import os
import csv
from ..state import get_current_db, get_current_data_path

def select(query: list):
    db_name = get_current_db()
    if not db_name:
        print("No database selected.")
        return

    db_path = os.path.join(get_current_data_path(), db_name)
    if not os.path.exists(db_path):
        print(f"Database '{db_name}' does not exist.")
        return

    try:
        if query[0].lower() == "select" and query[1].lower() == "count(*)" and query[2].lower() == "from":
            table_name = query[3].lower()
            table_file = os.path.join(db_path, f"{db_name}.{table_name}.csv")
            if not os.path.exists(table_file):
                print(f"Table '{table_name}' does not exist.")
                return
            with open(table_file, "r") as file:
                row_count = sum(1 for _ in file) - 1
            print(f"Row count: {row_count}")

        elif query[0].lower() == "select" and query[1] == "*" and query[2].lower() == "from":
            table_name = query[3].lower()
            table_file = os.path.join(db_path, f"{db_name}.{table_name}.csv")
            if not os.path.exists(table_file):
                print(f"Table '{table_name}' does not exist.")
                return
            output = []
            with open(table_file, "r") as file:
                if "where" in [q.lower() for q in query]:
                    where_index = [q.lower() for q in query].index("where")
                    condition = query[where_index + 1]
                    column, value = map(str.strip, condition.split("="))
                    column = column.lower()
                    value = value.lower()
                    reader = csv.DictReader(file, delimiter=';')
                    output.append(";".join(reader.fieldnames))
                    for row in reader:
                        # Ensure case-insensitive comparison for column values
                        if row.get(column, "").lower() == value:
                            output.append(";".join(row[field].strip() for field in reader.fieldnames))
                elif "like" in [q.lower() for q in query]:
                    like_index = [q.lower() for q in query].index("like")
                    pattern = query[like_index + 1].strip("'").strip('"').lower()
                    reader = csv.DictReader(file, delimiter=';')
                    output.append(";".join(reader.fieldnames))
                    for row in reader:
                        if any(pattern in cell.lower() for cell in row.values()):
                            output.append(";".join(row[field].strip() for field in reader.fieldnames))
                else:
                    reader = csv.reader(file, delimiter=';')
                    for row in reader:
                        output.append(";".join(row))
            print("\n".join(output))

        else:
            print("Unsupported query format.")

    except Exception as e:
        print(f"Error processing query: {e}")

if __name__ == "__main__":
    pass