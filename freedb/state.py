import os

# Global variable to store the current database
_current_db = None
_current_db_path = None
_current_data_path = None

def set_current_db(db_name, db_path):
    global _current_db, _current_db_path, _current_data_path
    _current_db = db_name
    _current_db_path = db_path

def set_curent_data_path(current_data_path):
    _current_data_path = current_data_path

def get_current_db():
    return _current_db

def get_current_db_path():
    return _current_db_path

def get_current_data_path():
    return _current_data_path

def clear_current_db():
    global _current_db, _current_db_path
    _current_db = None
    _current_db_path = None