from ..state import get_current_db, get_current_db_path

def create_table():
    db_name = get_current_db()
    db_path = get_current_db_path()
    print("Creating a new database entry...", db_path)

if __name__ == "__main__":
    #creat()
    pass