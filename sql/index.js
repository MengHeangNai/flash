import { PGlite } from "@electric-sql/pglite";
import fs from "fs";
import path from "path";

// const db = new PGlite("/Users/heang/Documents/native/python/sql/mydb.sqlite", {
//   mode: "readwrite",
//   version: "1.0.0",
//   schemaVersion: "1.0.0",
//   serializers: {
//     json: {
//       serialize: (value) => JSON.stringify(value),
//       deserialize: (value) => JSON.parse(value),
//     },
//   },
//   fileSizeLimit: 10 * 1024 * 1024, // 100 MB
// });

const db = new PGlite();

let initialized = false;
async function initDB() {
  if (initialized) return;

  await db.exec(`
      CREATE TABLE IF NOT EXISTS cars (
        id SERIAL PRIMARY KEY,
        brand TEXT,
        model TEXT,
        year INTEGER,
        price INTEGER,
        color TEXT,
        condition INTEGER,
        sold BOOLEAN
      );
  `);

  await db.exec(`
      INSERT INTO cars (brand, model, year, price, color, condition, sold) VALUES 
        ('Ford', 'Mustang', 1965, 45000, 'white', 4, false),
        ('Chevrolet', 'Camaro', 1970, 48000, 'red', 2, false),
        ('Dodge', 'Charger', 1969, 58000, 'black', 4, true),
        ('Porsche', '911', 1985, 85000, 'silver', 5, false),
        ('Jaguar', 'E-Type', 1967, 56000, 'green', 2, true),
        ('Jaguar', 'S-Type', 1963, 100000, 'dark green', 3, true),
        ('Jaguar', 'X-Type', 2001, 10000, 'black', 3, true),
        ('BMW', 'M3', 1990, 35000, 'green-yellow', 1, true),
        ('Ferrari', 'F355', 1997, 150000, 'red', 5, false),
        ('Ford', 'Mustang', 1967, 15000, 'dark blue', 0, false),
        ('Aston Martin', 'DB5', 1964, 595000, 'silver', 5, false),
        ('Aston Martin', 'DB4', 1960, 465000, 'light green', 5, false),
        ('Aston Martin', 'DBS', 1969, 99000, 'red', 2, false),
        ('Aston Martin', 'DB4', 1960, 425000, 'green', 3, false),
        ('Aston Martin', 'DB5', 1965, 649000, 'dark red', 5, false),
        ('Toyota', 'Supra', 1994, 68000, 'black', 4, true),
        ('Nissan', 'Skyline GT-R', 1999, 95000, 'blue', 5, false),
        ('Volkswagen', 'Beetle', 1963, 25000, 'yellow', 3, true),
        ('Lamborghini', 'Countach', 1989, 320000, 'red', 5, false),
        ('Rolls-Royce', 'Silver Shadow', 1975, 55000, 'white', 2, true),
        ('Bentley', 'Continental GT', 2005, 85000, 'black', 5, false),
        ('Maserati', 'GranTurismo', 2010, 75000, 'blue', 4, true),
        ('Alfa Romeo', 'Spider', 1986, 28000, 'red', 3, true),
        ('Ford', 'Mustang', 1965, 20000, 'dark red', 1, true),
        ('Lotus', 'Esprit', 1993, 62000, 'light yellow', 4, false),
        ('Triumph', 'Herald', 1965, 12500, 'cream', 3, true),
        ('Ford', 'Capri', 1983, 22000, 'blue', 2, false),
        ('Ford', 'Granada', 1977, 18000, 'black', 1, false),
        ('Volkswagen', 'Golf GTI', 1991, 12500, 'light green', 1, true),
        ('Chevrolet', 'Camaro', 1969, 54000, 'mint green', 5, true),
        ('Chevrolet', 'Corvette', 1967, 88000, 'red', 5, true),
        ('Chevrolet', 'Corvette C5', 2001, 32000, 'yellow', 4, true),
        ('Ferrari', 'Testarossa', 1988, 195000, 'red', 5, true),
        ('Ferrari', '360 Modena', 2003, 125000, 'silver', 5, true),
        ('Bentley', 'Arnage', 2001, 45000, 'black', 4, false),
        ('Bentley', 'Continental R', 1999, 68000, 'blue', 5, false),
        ('Jaguar', 'XJ220', 1994, 450000, 'silver', 5, false),
        ('Porsche', '911 Carrera', 1985, 85000, 'red', 5, false),
        ('Porsche', '911 Turbo', 1995, 12000, 'black', 1, false),
        ('Porsche', '944 Turbo', 1986, 48000, 'white', 4, true),
        ('Porsche', '356B', 1960, 265000, 'silver', 4, false),
        ('Bentley', 'T2', 1978, 52000, 'silver', 4, false);
  `);

  await db.exec(`
      CREATE INDEX IF NOT EXISTS idx_brand ON cars (brand);
      CREATE INDEX IF NOT EXISTS idx_model ON cars (model);
      CREATE INDEX IF NOT EXISTS idx_year ON cars (year);
      CREATE INDEX IF NOT EXISTS idx_color ON cars (color);
      CREATE INDEX IF NOT EXISTS idx_condition ON cars (condition);
      CREATE INDEX IF NOT EXISTS idx_sold ON cars (sold);
  `);

  await db.exec(`
      CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
      );
  `);

  await db.exec(`
      INSERT INTO users (username, password, email) VALUES
        ('admin', 'admin123', 'admin@example.com')
      `);
  initialized = true;
}

export const result = async (params = undefined) => {
  await initDB();
  // Load the SQL file
  const sqlPath = path.resolve("sql/query.sql");
  const query = fs.readFileSync(sqlPath, "utf8");

  const response = await db.query(queryParam(params, query));
  return response;
};

const queryParam = (params, query) => {
  const {
    brand,
    model,
    year,
    search,
    take,
    offset,
    orderBy = "id",
    order = "ASC",
  } = params || {};

  let conditions = [];

  if (brand) conditions.push(`brand = '${brand}'`);
  if (model) conditions.push(`model = '${model}'`);
  if (year) conditions.push(`year = ${year}`);

  if (search) {
    const searchCondition = `(
      brand ILIKE '%${search}%' OR
      model ILIKE '%${search}%' OR
      color ILIKE '%${search}%' OR
      year::text ILIKE '%${search}%'
    )`;
    conditions.push(searchCondition);
  }

  if (conditions.length) {
    query += " WHERE " + conditions.join(" AND ");
  }

  if (orderBy) {
    query += ` ORDER BY ${orderBy} ${order}`;
  }

  if (take) {
    query += ` LIMIT ${take}`;
  }

  if (offset) {
    query += ` OFFSET ${offset}`;
  }

  console.log("query :>> ", query);
  return query;
};
