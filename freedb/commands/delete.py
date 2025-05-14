from ..state import get_current_db, get_current_db_path
import os

def drop_table(table_name):
    db_path = get_current_db_path()
    file_name = get_current_db() + f'.{table_name}.csv'
    file_path = f'{db_path}\\{file_name}'
    print(db_path)
    print(file_path)
    deleted = False
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_name} gelöscht.")
        deleted = True
    else:
        print(f"{file_name} nicht gefunden.")

    if not deleted:
        print(f"Tabelle '{table_name}' konnte nicht gelöscht werden, da sie nicht existiert.")


if __name__ == "__main__":

    drop_table("")