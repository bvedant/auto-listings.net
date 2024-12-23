-- schema.sql
CREATE TABLE IF NOT EXISTS car_listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    mileage INTEGER NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    contact_email TEXT NOT NULL,
    date_posted TIMESTAMP NOT NULL
);

-- Create indexes for common search operations
CREATE INDEX IF NOT EXISTS idx_make_model ON car_listings(make, model);
CREATE INDEX IF NOT EXISTS idx_date_posted ON car_listings(date_posted);
CREATE INDEX IF NOT EXISTS idx_price ON car_listings(price);

-- Optional: Create a full-text search index if you want to implement more complex searching
-- CREATE VIRTUAL TABLE IF NOT EXISTS car_listings_fts USING fts5(
--     title, make, model, description,
--     content='car_listings',
--     content_rowid='id'
-- );

-- Optional: Create a trigger to keep the FTS index up to date
-- CREATE TRIGGER IF NOT EXISTS car_listings_ai AFTER INSERT ON car_listings BEGIN
--     INSERT INTO car_listings_fts(rowid, title, make, model, description)
--     VALUES (new.id, new.title, new.make, new.model, new.description);
-- END;