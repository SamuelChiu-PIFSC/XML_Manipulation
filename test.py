import json
from pathlib import Path

import duckdb
import xmltodict

def get_keys_at_depth(data, target_depth, current_depth=1):
    """Traverses a nested dict/list and returns unique keys found at `target_depth`."""
    keys = set()

    # Base case: we reached our target depth
    if current_depth == target_depth:
        if isinstance(data, dict):
            return set(data.keys())
        return set()

    # Recursive case: dive deeper
    if current_depth < target_depth:
        if isinstance(data, dict):
            for value in data.values():
                keys.update(
                    get_keys_at_depth(value, target_depth, current_depth + 1)
                )
        elif isinstance(data, list):
            for item in data:
                keys.update(
                    get_keys_at_depth(item, target_depth, current_depth)
                )

    return keys






BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / "data_archival.db"
xml_file_path = BASE_DIR / "inport-xml.xml"

with open(xml_file_path, encoding="utf-8") as f:
    parsed_dict = xmltodict.parse(f.read())

print(parsed_dict)



