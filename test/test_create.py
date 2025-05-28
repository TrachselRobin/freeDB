import freedb as db
import pytest
from pathlib import Path
import csv

@pytest.fixture
def test_env(tmp_path):
    data_dir = tmp_path / "test_data"
    db.config_data_path(str(data_dir))
    return data_dir

def test_create_database(test_env):
    db.create_database("neue_db")
    db_path = test_env / "neue_db"
    assert db_path.exists()
    assert db.get_current_db() == "neue_db"

def test_create_table(test_env):
    db.create_database("neue_db")
    db.use("neue_db")

    db.create_table("personen", ["id", "name", "alter"])
    db_path = test_env / "neue_db"

    structure = db_path / "neue_db.personen.structure.csv"
    content = db_path / "neue_db.personen.content.csv"

    assert structure.exists()
    assert content.exists()

    with open(structure, newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        assert headers == ["id", "name", "alter"]

def test_insert_and_sort(test_env):
    db.create_database("neue_db")
    db.use("neue_db")
    db.create_table("personen", ["id", "name"])

    # Reihenfolge absichtlich ungeordnet
    db.insert(["personen", "values", "3", "Clara"])
    db.insert(["personen", "values", "1", "Anna"])
    db.insert(["personen", "values", "2", "Ben"])

    content_path = test_env / "neue_db" / "neue_db.personen.content.csv"
    with open(content_path, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows[0] == ["id", "name"]  # Header
    assert rows[1:] == [["1", "Anna"], ["2", "Ben"], ["3", "Clara"]]
