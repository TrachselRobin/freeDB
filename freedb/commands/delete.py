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


def delete_query(table_name, field, value):
    db_path = get_current_db_path()
    file_name = get_current_db() + f'.{table_name}.csv'
    file_path = f'{db_path}\\{file_name}'
    temp_file = get_current_db() + f".{table_name}.tmp"

    if not os.path.exists(file_path):
        print(f"Tabelle '{table_name}' existiert nicht.")
        return

    with open(file_path, 'r') as infile, open(temp_file, 'w') as outfile:
        lines = infile.readlines()
        header = lines[0].strip().split(';')

        if field not in header:
            print(f"Fehler: Spalte '{field}' existiert nicht in '{table_name}'.")
            return

        col_index = header.index(field)
        outfile.write(lines[0])
        removed = 0
        for line in lines[1:]:
            row = line.strip().split(';')
            if row[col_index] != value:
                outfile.write(line)
            else:
                removed += 1

    os.replace(temp_file, file_path)
    print(f"{removed} Zeile(n) mit {field} = {value} aus '{table_name}' gelöscht.")

