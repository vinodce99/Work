import datetime as dt
import json

def get_current_time():
    """Returns the current time in ISO 8601 format."""
    return dt.datetime.now().isoformat()

def save_to_json(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f)