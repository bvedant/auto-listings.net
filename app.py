# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, g
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
DATABASE = 'cars.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # This allows accessing columns by name
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def home():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM car_listings 
        ORDER BY date_posted DESC
    ''')
    listings = cursor.fetchall()
    return render_template('index.html', listings=listings)

@app.route('/listing/new', methods=['GET', 'POST'])
def new_listing():
    if request.method == 'POST':
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('''
                INSERT INTO car_listings (
                    title, make, model, year, mileage, 
                    price, description, contact_email, date_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                request.form['title'],
                request.form['make'],
                request.form['model'],
                request.form['year'],
                request.form['mileage'],
                request.form['price'],
                request.form['description'],
                request.form['contact_email'],
                datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            ))
            db.commit()
            flash('Your listing has been created!', 'success')
            return redirect(url_for('home'))
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('listing'))

    return render_template('listing.html')

@app.route('/listing/<int:listing_id>')
def listing(listing_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM car_listings WHERE id = ?', (listing_id,))
    listing = cursor.fetchone()
    if listing is None:
        return 'Listing not found', 404
    return render_template('listing.html', listing=listing)

@app.route('/listing/<int:listing_id>/delete', methods=['POST'])
def delete_listing(listing_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM car_listings WHERE id = ?', (listing_id,))
        db.commit()
        flash('Listing deleted successfully', 'success')
    except sqlite3.Error as e:
        flash(f'An error occurred: {e}', 'error')
    return redirect(url_for('home'))

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        db = get_db()
        cursor = db.cursor()
        search_param = f'%{query}%'
        cursor.execute('''
            SELECT * FROM car_listings 
            WHERE title LIKE ? 
            OR make LIKE ? 
            OR model LIKE ? 
            OR description LIKE ?
            ORDER BY date_posted DESC
        ''', (search_param, search_param, search_param, search_param))
        listings = cursor.fetchall()
    else:
        listings = []
    return render_template('index.html', listings=listings, search_query=query)

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
