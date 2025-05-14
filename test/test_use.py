# test/test_use.py
import freedb as db

def test_use_output(capsys, tmp_path):
    data_dir = tmp_path / "temp_data"
    data_dir.mkdir()
    db_folder = data_dir / "test"
    db_folder.mkdir()
    db.use("test", data_dir=str(data_dir))
    captured = capsys.readouterr()
    expected_path = str(data_dir / "test")
    assert f"Switched to database: test (Location: {expected_path})" in captured.out

if __name__ == "__main__":
    test_use_output()