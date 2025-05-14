# test/test_config.py
import freedb as db
import pytest

def test_config(capsys, tmp_path):
    data_dir = tmp_path / "temp_data"
    data_dir.mkdir()
    db_folder = data_dir / "test"
    db_folder.mkdir()
    db.config_data_path(str(data_dir))
    db.use("test")
    captured = capsys.readouterr()
    expected_path = str(data_dir / "test")
    assert f"Data directory updated to: {str(data_dir)}" in captured.out

def test_config_persistence(capsys, tmp_path):
    data_dir = tmp_path / "temp_data"
    data_dir.mkdir()
    db.config_data_path(str(data_dir))
    captured = capsys.readouterr()
    assert f"Data directory updated to: {str(data_dir)}" in captured.out
    # Simulate a new session by reloading the module
    import importlib
    importlib.reload(db)
    assert db.get_current_data_path() == str(data_dir)

def test_config_invalid_path(capsys):
    invalid_path = "Z:/nonexistent_path"
    db.config_data_path(invalid_path)
    captured = capsys.readouterr()
    assert f"Data directory updated to: {invalid_path}" in captured.out
    assert db.get_current_data_path() == invalid_path

if __name__ == "__main__":
    test_config()
    test_config_persistence()
    test_config_invalid_path()