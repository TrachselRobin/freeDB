# test/test_use.py
import freedb as db

def test_use_output(capsys, tmp_path):
    data_dir = tmp_path / "temp_data"
    data_dir.mkdir()
    db_folder = data_dir / "test"
    db_folder.mkdir()
    db.use("test", data_dir=str(data_dir))

def test_use_nonexistent_db(capsys, tmp_path):
    data_dir = tmp_path / "temp_data"
    data_dir.mkdir()
    db.config_data_path(str(data_dir))
    db.use("nonexistent_db")
    captured = capsys.readouterr()
    expected_path = str(data_dir / "nonexistent_db")
    assert f"Database 'nonexistent_db' not found at {expected_path}" in captured.out

def test_use_switch_db(capsys, tmp_path):
    data_dir = tmp_path / "temp_data"
    data_dir.mkdir()
    db_folder1 = data_dir / "db1"
    db_folder2 = data_dir / "db2"
    db_folder1.mkdir()
    db_folder2.mkdir()
    db.config_data_path(str(data_dir))
    db.use("db1")
    captured1 = capsys.readouterr()
    assert f"Switched to database: db1" in captured1.out
    db.use("db2")
    captured2 = capsys.readouterr()
    assert f"Switched to database: db2" in captured2.out

if __name__ == "__main__":
    test_use_output()
    test_use_nonexistent_db()
    test_use_switch_db()