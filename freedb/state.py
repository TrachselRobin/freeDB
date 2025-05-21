import os
import json

# Global variable to store the current database
_current_db = None
_current_db_path = None
_current_data_path = None
CONFIG_FILE = "freedb_config.json"

def _load_config():
    global _current_db, _current_db_path, _current_data_path
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            _current_data_path = config.get("data_path")
            _current_db = config.get("current_db")
            if _current_db:
                _current_db_path = os.path.join(_current_data_path, _current_db)
    else:
        _current_data_path = os.path.abspath(os.path.join(os.getcwd(), "data"))

def _save_config():
    config = {
        "data_path": _current_data_path,
        "current_db": _current_db
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def set_current_db(db_name):
    global _current_db, _current_db_path
    if db_name is None:
        _load_config()
        return
    _current_db = db_name
    _current_db_path = os.path.join(_current_data_path, db_name)
    _save_config()

def set_current_data_path(current_data_path):
    global _current_data_path, _current_db_path
    if current_data_path is None:
        _load_config()
        return
    _current_data_path = current_data_path
    if _current_db:
        _current_db_path = os.path.join(_current_data_path, _current_db)
    _save_config()

def get_current_db():
    if _current_db is None:
        _load_config()
    return _current_db

def get_current_db_path():
    if _current_db_path is None:
        _load_config()
    return _current_db_path

def get_current_data_path():
    if _current_data_path is None:
        _load_config()
    return _current_data_path

def clear_current_db():
    global _current_db, _current_db_path
    _current_db = None
    _current_db_path = None
    _save_config()

# Initialize the configuration on module load
_load_config()
