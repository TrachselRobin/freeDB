import sys

from .state import set_current_data_path, get_current_data_path, get_current_db, get_current_db_path
from .commands import config_data_path, create_table, create_database, insert, drop_table, delete_query, select, update, use


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m freedb <command> [args]")
        sys.exit(1)

    command = sys.argv[1].lower()
    arg2 = sys.argv[2].lower()
    commands = {
        "config": {
            "path": lambda: config_data_path(sys.argv[3])
        },
        "create": {
            "table": lambda: create_table(sys.argv[3], sys.argv[5:])
                if len(sys.argv) > 4 and sys.argv[4].lower() == "columns"
                else create_table(sys.argv[3]),
            "database": lambda: create_database(sys.argv[3]) if len(sys.argv) > 3 else print("Missing database name."),
            "db": lambda: create_database(sys.argv[3]) if len(sys.argv) > 3 else print("Missing database name."),
        },
        "delete": {
            "table": lambda: drop_table(arg2),
            "query": lambda: delete_query(*sys.argv[2:]),
        },
        "insert": lambda: insert(sys.argv[2:]),
        "read": select,
        "update": update,
        "use": lambda: use(sys.argv[2], None if len(sys.argv) <= 3 else sys.argv[3]),
    }

    if command in commands:
        if isinstance(commands[command], dict):
            commands[command][arg2]()
        else:
            commands[command]()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
