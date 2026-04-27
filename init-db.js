require('dotenv').config();
const { Pool } = require('pg');
const fs = require('fs');
const path = require('path');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

async function initDB() {
  const client = await pool.connect();
  try {
    console.log('Connecting to Postgres database...');

    // 1. Create table
    await client.query(`
      CREATE TABLE IF NOT EXISTS menu_items (
        id SERIAL PRIMARY KEY,
        menu_type VARCHAR(20) NOT NULL,
        category VARCHAR(100) NOT NULL,
        name_en VARCHAR(255),
        name_ar VARCHAR(255),
        desc_en TEXT,
        desc_ar TEXT,
        price NUMERIC(10, 2) NOT NULL,
        order_index INT DEFAULT 0
      );
    `);
    
    // Clear old data to prevent duplicates (optional)
    await client.query('TRUNCATE TABLE menu_items RESTART IDENTITY;');

    console.log('Table created successfully. Inserting data...');

    // 2. Read Local JSON files
    const sohoData = JSON.parse(fs.readFileSync(path.join(__dirname, 'soho_items.json'), 'utf8'));
    const istikData = JSON.parse(fs.readFileSync(path.join(__dirname, 'istik_items.json'), 'utf8'));

    // 3. Insert Soho
    let orderIndex = 0;
    for (const [category, items] of Object.entries(sohoData)) {
      for (const item of items) {
        // Fallbacks for Arabic descriptions that might be object keys
        const descAr = typeof item.descAr === 'object' ? JSON.stringify(item.descAr) : item.descAr || '';
        
        await client.query(
          `INSERT INTO menu_items (menu_type, category, name_en, name_ar, desc_en, desc_ar, price, order_index)
           VALUES ($1, $2, $3, $4, $5, $6, $7, $8)`,
          ['soho', category, item.name || '', item.nameAr || '', item.desc || '', descAr, item.price || 0, orderIndex++]
        );
      }
    }

    // 4. Insert Istik
    for (const [category, items] of Object.entries(istikData)) {
      for (const item of items) {
        await client.query(
          `INSERT INTO menu_items (menu_type, category, name_en, name_ar, desc_en, desc_ar, price, order_index)
           VALUES ($1, $2, $3, $4, $5, $6, $7, $8)`,
          ['istik', category, item.name || '', item.nameAr || '', item.desc || '', item.descAr || '', item.price || 0, orderIndex++]
        );
      }
    }

    console.log('Database seeded successfully from JSON files!');
  } catch (err) {
    console.error('Error initializing database:', err);
  } finally {
    client.release();
    pool.end();
  }
}

initDB();
