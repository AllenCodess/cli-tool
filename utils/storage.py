import json
import os
from models.user import User

DATA_FILE = "data/db.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            users_data = json.load(f)
            return [User.from_dict(u) for u in users_data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(users):
    with open(DATA_FILE, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=4)
