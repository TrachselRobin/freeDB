import sys
from .commands import create_table, create_database, insert, delete, read, update, use


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m freedb <command> [args]")
        sys.exit(1)

    command = sys.argv[1].lower()
    arg2 = sys.argv[2].lower()
    commands = {
        "insert": insert,
        "create": {
            # name is the next arg
            "table": lambda: create_table(sys.argv[3]) if len(sys.argv) > 3 else print("Missing table name."),
            "database": lambda: create_database(sys.argv[3]) if len(sys.argv) > 3 else print("Missing database name.")
        },
        "delete": delete,
        "read": read,
        "update": update,
        "use": lambda: use(sys.argv[2], None if sys.argv[3] is None else sys.argv[3])
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