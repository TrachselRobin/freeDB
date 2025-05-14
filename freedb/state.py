import os
import json

# Global variable to store the current database
_current_db = None
_current_db_path = None
_current_data_path = None
CONFIG_FILE = "freedb_config.json"

<<<<<<< HEAD
def _load_config():
    global _current_data_path
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            _current_data_path = config.get("data_path")
    else:
        _current_data_path = os.path.abspath(os.path.join(os.getcwd(), "data"))

def _save_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump({"data_path": _current_data_path}, f)

def set_current_db(db_name):
=======
def set_current_db(db_name, db_path):
>>>>>>> 5313faf16d43237cef23d1f37ffe1a9d8bc6ac99
    global _current_db, _current_db_path
    _current_db = db_name
    _current_db_path = f"{_current_data_path}/{db_name}"

def set_curent_data_path(current_data_path):
    global _current_data_path
    _current_data_path = current_data_path
    _save_config()  # Save the updated data path to the config file

def get_current_db():
    return _current_db

def get_current_db_path():
    return _current_db_path

def get_current_data_path():
    if _current_data_path is None:
        _load_config()  # Load the data path from the config file if not already loaded
    return _current_data_path

def clear_current_db():
    global _current_db, _current_db_path
    _current_db = None
    _current_db_path = None

# Initialize the configuration on module load
_load_config()