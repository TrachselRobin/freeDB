from ..state import set_current_data_path

def config_data_path(path: str):
    set_current_data_path(path)
    print(f"Data directory updated to: {path}")

if __name__ == "__main__":
    pass