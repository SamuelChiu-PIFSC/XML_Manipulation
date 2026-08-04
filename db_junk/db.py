from pathlib import Path

import duckdb

# Get the directory where the current Python script is located
BASE_DIR = Path(__file__).resolve().parent

# Define the database path relative to the script's directory
db_path = BASE_DIR / "data_archival.db"

# Connect using the OS-agnostic path (converted to string)
con = duckdb.connect(str(db_path))

