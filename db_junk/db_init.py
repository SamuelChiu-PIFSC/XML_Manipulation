from pathlib import Path

import duckdb

# Define database location
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / "data_archival.db"

def init_database():
    with duckdb.connect(db_path) as con:
        # ----------------------------------------------------
        # 1. CREATE TABLES
        # ----------------------------------------------------
        
        # Table 1: Categories
        con.execute("""
            CREATE TABLE IF NOT EXISTS survey_categories (
                category_id   INTEGER PRIMARY KEY,
                category_name VARCHAR NOT NULL UNIQUE,
                description   VARCHAR
            );
        """)

        # Table 2: File Catalog & Metadata
        con.execute("""
            CREATE TABLE IF NOT EXISTS files (
                file_id       INTEGER PRIMARY KEY,
                category_id   INTEGER REFERENCES survey_categories(category_id),
                file_name     VARCHAR NOT NULL,
                file_type     VARCHAR NOT NULL,
                keywords      VARCHAR[],  -- Native array for search tags
                metadata      JSON,       -- Flexible custom attributes
                created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Table 3: Sample Data Previews (Stored in DB)
        con.execute("""
            CREATE TABLE IF NOT EXISTS sample_datasets (
                sample_id   INTEGER PRIMARY KEY,
                file_id     INTEGER REFERENCES files(file_id),
                sample_data JSON NOT NULL
            );
        """)

        print("Database schema initialized successfully!")

if __name__ == "__main__":
    init_database()