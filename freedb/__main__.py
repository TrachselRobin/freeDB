import sys
from .commands import create, delete, read, update, use

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m freedb <command> [args]")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    commands = {
        "create": create,
        "delete": delete,
        "read": read,
        "update": update,
        "use": lambda: use(sys.argv[2])
    }
    
    if command in commands:
        commands[command]()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()