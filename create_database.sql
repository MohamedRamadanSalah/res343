-- PostgreSQL Database Setup for Menu System
-- Database: men_database

-- DROP existing tables if they exist (uncomment to recreate)
-- DROP TABLE IF EXISTS translations CASCADE;
-- DROP TABLE IF EXISTS items CASCADE;
-- DROP TABLE IF EXISTS categories CASCADE;
-- DROP TABLE IF EXISTS restaurants CASCADE;

-- Create restaurants table
CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    name_ar VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create categories table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER NOT NULL REFERENCES restaurants(id) ON DELETE CASCADE,
    name_ar VARCHAR(255) NOT NULL,
    name_en VARCHAR(255),
    display_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(restaurant_id, name_ar)
);

-- Create items table (menu items)
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    restaurant_id INTEGER NOT NULL REFERENCES restaurants(id) ON DELETE CASCADE,
    name_ar VARCHAR(255) NOT NULL,
    name_en VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    description_ar TEXT,
    description_en TEXT,
    is_available BOOLEAN DEFAULT true,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(category_id, name_ar)
);

-- Create translations table (for quick lookup)
CREATE TABLE translations (
    id SERIAL PRIMARY KEY,
    arabic_text VARCHAR(500) NOT NULL UNIQUE,
    english_text VARCHAR(500),
    context VARCHAR(50), -- 'item', 'category', 'restaurant'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX idx_items_restaurant_id ON items(restaurant_id);
CREATE INDEX idx_items_category_id ON items(category_id);
CREATE INDEX idx_categories_restaurant_id ON categories(restaurant_id);
CREATE INDEX idx_translations_arabic ON translations(arabic_text);
CREATE INDEX idx_items_is_available ON items(is_available);

-- Insert restaurants
INSERT INTO restaurants (name, name_ar) VALUES
('Istiknanah', 'استكنانة'),
('Soho', 'سوهو');

-- Note: Run the Node.js data import script next to populate categories and items
-- from your JSON files
