import sys
from .state import set_curent_data_path, get_current_data_path, get_current_db, get_current_db_path
from .commands import config_data_path, create_table, delete, read, update, use

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
            "table": create_table,
        },
        "delete": delete,
        "read": read,
        "update": update,
        "use": lambda: use(sys.argv[2], None if len(sys.argv) <= 3 else sys.argv[3])
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