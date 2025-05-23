import os
import csv
from ..state import get_current_db, get_current_db_path, get_current_data_path, set_current_db

def create_database(database_name):
    base_path = get_current_data_path()
    db_path = os.path.join(base_path, database_name)

    if os.path.exists(db_path):
        print(f"Fehler: Datenbank '{database_name}' existiert bereits unter {db_path}")
        return

    os.makedirs(db_path)
    set_current_db(database_name)
    print(f"Datenbank '{database_name}' wurde erstellt unter {db_path}.")

def create_table(table_name, columns=None):
    db_name = get_current_db()
    db_path = get_current_db_path()
    if not db_name:
        print("Fehler: Keine Datenbank ausgewählt.")
        return

    structure_file = os.path.join(db_path, f"{db_name}.{table_name}.structure.csv")
    content_file = os.path.join(db_path, f"{db_name}.{table_name}.content.csv")

    if os.path.exists(structure_file) or os.path.exists(content_file):
        print(f"Fehler: Tabelle '{table_name}' existiert bereits.")
        return

    if columns is None:
        print("Gib die Spaltennamen ein, durch Komma getrennt (z.B. id,name,age): ")
        header = str(input()).strip()
        columns = [col.strip() for col in header.split(',') if col.strip()]
    else:
        columns = [col.strip() for col in columns if col.strip()]

    if not columns:
        print("Fehler: Keine gültigen Spaltennamen eingegeben.")
        return

    with open(structure_file, 'w', newline='') as sfile, open(content_file, 'w', newline='') as cfile:
        writer = csv.writer(sfile)
        writer.writerow(columns)
        writer = csv.writer(cfile)
        writer.writerow(columns)

    print(f"Tabelle '{table_name}' wurde mit Spalten {columns} erstellt.")


def insert(args=None):
    db_name = get_current_db()
    db_path = get_current_db_path()
    if not db_name:
        print("Fehler: Keine Datenbank ausgewählt.")
        return

    if not args or len(args) < 3 or args[1].lower() != "values":
        print("Verwendung: python -m freedb insert <tabelle> values <wert1> <wert2> ...")
        return

    table_name = args[0]
    values = args[2:]

    structure_file = os.path.join(db_path, f"{db_name}.{table_name}.structure.csv")
    content_file = os.path.join(db_path, f"{db_name}.{table_name}.content.csv")

    if not os.path.exists(structure_file) or not os.path.exists(content_file):
        print(f"Fehler: Tabelle '{table_name}' existiert nicht.")
        return

    with open(structure_file, 'r') as sfile:
        reader = csv.reader(sfile)
        columns = next(reader)

    if len(values) != len(columns):
        print(f"Fehler: Anzahl der Werte ({len(values)}) stimmt nicht mit der Anzahl der Spalten ({len(columns)}) überein.")
        return

    with open(content_file, 'a', newline='') as cfile:
        writer = csv.writer(cfile)
        writer.writerow(values)

    # Sortieren nach der ersten Spalte
    with open(content_file, 'r') as cfile:
        lines = list(csv.reader(cfile))
    header, rows = lines[0], lines[1:]
    rows.sort(key=lambda x: x[0])

    with open(content_file, 'w', newline='') as cfile:
        writer = csv.writer(cfile)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Eintrag in '{table_name}' erfolgreich hinzugefügt und sortiert.")


if __name__ == "__main__":
    pass
