# test/test_use.py
import freedb as db

def test_use_output(capsys):
    data_dir = tmp_path / "temp_data"
    data_dir.mkdir()
    db_folder = data_dir / "test"
    db_folder.mkdir()
    db.use("test", data_dir=str(data_dir))
    db.drop_table("testDatabase.users.csv")

if __name__ == "__main__":
    test_use_output()