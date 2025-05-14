import os
from ..state import set_current_db, get_current_db

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), "data"))

def use(db_name, data_dir: str = None):
    """Set the current database to the specified name."""
    if data_dir is not None:
        BASE_DIR = os.path.abspath(data_dir)
    db_path = os.path.join(BASE_DIR, f"{db_name}")
    
    if not os.path.exists(db_path):
        print(f"Database '{db_name}' not found at {db_path}")
        return

    set_current_db(db_name, db_path)
    print(f"Switched to database: {db_name} (Location: {db_path})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m freedb use <db_name>")
        sys.exit(1)
    use(sys.argv[1])