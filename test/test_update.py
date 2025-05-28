import freedb as db
import pytest
from pathlib import Path
import csv

@pytest.fixture
def setup_test_db(tmp_path):
    data_dir = tmp_path / "test_data"
    data_dir.mkdir()
    db_folder = data_dir / "test_db"
    db_folder.mkdir()
    db.config_data_path(str(data_dir))
    db.use("test_db")

    structure_file = db_folder / "test_db.users.structure.csv"
    content_file = db_folder / "test_db.users.content.csv"

    headers = "ID;Vorname;Nachname;Email;Geburtsjahr;Kanton\n"
    rows = [
        "1;Anna;Muster;anna.muster@example.com;1990;Zurich\n",
        "2;Ben;Huber;ben.huber@example.com;1985;Aargau\n",
        "3;Clara;Meier;clara.meier@example.com;1992;Zurich\n"
    ]

    structure_file.write_text(headers)
    content_file.write_text(headers + "".join(rows))

    return content_file  # gibt den content_file zurück für Testzwecke


def test_update_value(setup_test_db):
    # Simuliere Kommandozeilenargumente für update()
    db.update(["", "users", "set", "Kanton=Bern", "where", "Vorname=Clara"])

    # Prüfen ob Clara jetzt in "Bern" ist
    with open(setup_test_db, newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row["Vorname"] == "Clara":
                assert row["Kanton"] == "Bern"

def test_alter_add_column(setup_test_db):
    db.alter_add_column("users", "Status")

    with open(setup_test_db, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        headers = next(reader)
        assert "Status" in headers

        for row in reader:
            assert len(row) == len(headers)
            assert row[-1] == ""  # Neue Spalte leer
