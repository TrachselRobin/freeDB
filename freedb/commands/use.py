import os
from ..state import set_current_db, get_current_data_path, set_current_data_path

def use(db_name, data_dir: str = None):
    """Set the current database to the specified name."""
    if data_dir is not None:
        data_dir = os.path.abspath(data_dir)
        set_current_data_path(data_dir)
        base = data_dir
    else:
        base = get_current_data_path() or os.path.abspath(os.path.join(os.getcwd(), "data"))  # Ensure base is initialized

    db_path = os.path.join(base, db_name)

    if not os.path.exists(db_path):
        print(f"Database '{db_name}' not found at {db_path}")
        return

    set_current_db(db_name)
    print(f"Switched to database: {db_name} (Location: {db_path})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m freedb use <db_name>")
        sys.exit(1)
    use(sys.argv[1])