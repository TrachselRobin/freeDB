from ..state import get_current_db, get_current_db_path, get_current_data_path

def create_table(table_name):
    db_name = get_current_db()
    db_path = get_current_db_path()
    data_path = get_current_data_path()

    print(db_name, table_name, db_path, data_path)

def create_database(database_name):
    db_name = get_current_db()
    db_path = get_current_db_path()
    data_path = get_current_data_path()

    print(db_name, database_name, db_path, data_path)

def insert():
    db_name = get_current_db()
    db_path = get_current_db_path()

if __name__ == "__main__":
    #creat()
    pass