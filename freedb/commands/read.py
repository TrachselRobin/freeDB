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
        if len(query) >= 4 and query[0].lower() == "select" and query[1].lower() == "count(*)" and query[2].lower() == "from":
            table_name = query[3].lower()
            table_file = os.path.join(db_path, f"{db_name}.{table_name}.content.csv")
            if not os.path.exists(table_file):
                print(f"Table '{table_name}' does not exist.")
                return
            with open(table_file, "r", newline='') as file:
                row_count = sum(1 for _ in file) - 1
            print(f"Row count: {row_count}")
            return

        if len(query) >= 4 and query[0].lower() == "select" and query[1] == "*" and query[2].lower() == "from":
            table_name = query[3].lower()
            table_file = os.path.join(db_path, f"{db_name}.{table_name}.content.csv")
            if not os.path.exists(table_file):
                print(f"Table '{table_name}' does not exist.")
                return

            with open(table_file, "r", newline='') as file:
                reader = csv.DictReader(file)  # default delimiter=','
                output = []
                output.append(','.join(reader.fieldnames))

                lower_q = [q.lower() for q in query]
                file.seek(0)
                reader = csv.DictReader(file)

                if "where" in lower_q:
                    where_idx = lower_q.index("where")
                    if where_idx + 1 < len(query):
                        condition = query[where_idx + 1].strip("'\"")
                        if "=" in condition:
                            column, value = map(str.strip, condition.split("=", 1))
                            column = column.lower()
                            value = value.lower()
                            for row in reader:
                                if row.get(column, "").lower() == value:
                                    output.append(','.join(row[field].strip() for field in reader.fieldnames))

                elif "like" in lower_q:
                    like_idx = lower_q.index("like")
                    if like_idx + 1 < len(query):
                        pattern = query[like_idx + 1].strip("'\"").lower()
                        for row in reader:
                            if any(pattern in cell.lower() for cell in row.values()):
                                output.append(','.join(row[field].strip() for field in reader.fieldnames))

                else:
                    for row in reader:
                        output.append(','.join(row[field].strip() for field in reader.fieldnames))

            print("\n".join(output))
            return

        print("Unsupported query format.")

    except Exception as e:
        print(f"Error processing query: {e}")

if __name__ == "__main__":
    pass
