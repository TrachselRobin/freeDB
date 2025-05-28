import os
import csv
from ..state import get_current_db, get_current_db_path

def update(args):
    if len(args) < 6:
        print("Verwendung: python -m freedb update <tabelle> set <spalte>=<wert> where <spalte>=<wert>")
        return

    _, table_name, set_kw, set_expr, where_kw, where_expr = args

    if set_kw.lower() != "set" or where_kw.lower() != "where":
        print("Verwendung: ... set <spalte>=<wert> where <spalte>=<wert>")
        return

    set_column, set_value = map(str.strip, set_expr.split("="))
    where_column, where_value = map(str.strip, where_expr.split("="))

    db_name = get_current_db()
    db_path = get_current_db_path()
    file_path = os.path.join(db_path, f"{db_name}.{table_name}.content.csv")

    if not os.path.exists(file_path):
        print(f"Tabelle '{table_name}' existiert nicht.")
        return

    updated = 0
    temp_path = file_path + ".tmp"

    with open(file_path, 'r', newline='') as infile, open(temp_path, 'w', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter=';')
        fieldnames = reader.fieldnames
        if set_column not in fieldnames or where_column not in fieldnames:
            print("Fehler: Ungültige Spalte.")
            return

        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        for row in reader:
            if row[where_column] == where_value:
                row[set_column] = set_value
                updated += 1
            writer.writerow(row)

    os.replace(temp_path, file_path)
    print(f"{updated} Zeile(n) aktualisiert.")

def alter_add_column(table_name, new_column):
    db_name = get_current_db()
    db_path = get_current_db_path()
    structure_file = os.path.join(db_path, f"{db_name}.{table_name}.structure.csv")
    content_file = os.path.join(db_path, f"{db_name}.{table_name}.content.csv")

    if not os.path.exists(structure_file) or not os.path.exists(content_file):
        print(f"Fehler: Tabelle '{table_name}' existiert nicht.")
        return

    with open(structure_file, 'r', newline='') as sfile:
        reader = csv.reader(sfile)
        headers = next(reader)
        if new_column in headers:
            print(f"Spalte '{new_column}' existiert bereits.")
            return

    headers.append(new_column)
    with open(structure_file, 'w', newline='') as sfile:
        writer = csv.writer(sfile, delimiter=';')

        writer.writerow(headers)

    updated_rows = []
    with open(content_file, 'r', newline='') as cfile:
        reader = csv.reader(cfile)
        content_headers = next(reader)
        rows = [row + [''] for row in reader]

    with open(content_file, 'w', newline='') as cfile:
        writer = csv.writer(cfile, delimiter=';')

        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Spalte '{new_column}' zur Tabelle '{table_name}' hinzugefügt.")

if __name__ == "__main__":
    pass
