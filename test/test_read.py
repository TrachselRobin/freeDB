import freedb as db
import pytest
from pathlib import Path

@pytest.fixture
def setup_test_db(tmp_path):
    data_dir = tmp_path / "test_data"
    data_dir.mkdir()
    db_folder = data_dir / "test_db"
    db_folder.mkdir()
    db.config_data_path(str(data_dir))
    db.use("test_db")
    table_file = db_folder / "test_db.users.csv"
    table_file.write_text(
        "ID;Vorname;Nachname;Email;Geburtsjahr;Kanton\n"
        "1;Anna;Muster;anna.muster@example.com;1990;Zurich\n"
        "2;Ben;Huber;ben.huber@example.com;1985;Aargau\n"
        "3;Clara;Meier;clara.meier@example.com;1992;Zurich\n"
        "4;Daniel;Schmidt;daniel.schmidt@example.com;1980;Jura\n"
        "5;Elif;Kaya;elif.kaya@example.com;1995;Jura\n"
    )
    return table_file

def test_select_all(setup_test_db, capsys):
    db.select(["SELECT", "*", "FROM", "users"])
    captured = capsys.readouterr()
    assert "ID;Vorname;Nachname;Email;Geburtsjahr;Kanton" in captured.out
    assert "1;Anna;Muster;anna.muster@example.com;1990;Zurich" in captured.out
    assert "2;Ben;Huber;ben.huber@example.com;1985;Aargau" in captured.out
    assert "3;Clara;Meier;clara.meier@example.com;1992;Zurich" in captured.out
    assert "4;Daniel;Schmidt;daniel.schmidt@example.com;1980;Jura" in captured.out
    assert "5;Elif;Kaya;elif.kaya@example.com;1995;Jura" in captured.out

def test_select_count(setup_test_db, capsys):
    db.select(["SELECT", "COUNT(*)", "FROM", "users"])
    captured = capsys.readouterr()
    assert "Row count: 5" in captured.out

def test_select_where(setup_test_db, capsys):
    db.select(["SELECT", "*", "FROM", "users", "WHERE", "Vorname=Anna"])
    captured = capsys.readouterr()
    assert "ID;Vorname;Nachname;Email;Geburtsjahr;Kanton" in captured.out
    assert "1;Anna;Muster;anna.muster@example.com;1990;Zurich" in captured.out
    assert "2;Ben;Huber;ben.huber@example.com;1985;Aargau" not in captured.out
    assert "3;Clara;Meier;clara.meier@example.com;1992;Zurich" not in captured.out
    assert "4;Daniel;Schmidt;daniel.schmidt@example.com;1980;Jura" not in captured.out
    assert "5;Elif;Kaya;elif.kaya@example.com;1995;Jura" not in captured.out

def test_select_like(setup_test_db, capsys):
    db.select(["SELECT", "*", "FROM", "users", "LIKE", "'anna'"])
    captured = capsys.readouterr()
    assert "ID;Vorname;Nachname;Email;Geburtsjahr;Kanton" in captured.out
    assert "1;Anna;Muster;anna.muster@example.com;1990;Zurich" in captured.out
    assert "2;Ben;Huber;ben.huber@example.com;1985;Aargau" not in captured.out
    assert "3;Clara;Meier;clara.meier@example.com;1992;Zurich" not in captured.out
    assert "4;Daniel;Schmidt;daniel.schmidt@example.com;1980;Jura" not in captured.out
    assert "5;Elif;Kaya;elif.kaya@example.com;1995;Jura" not in captured.out

def test_select_invalid_query(setup_test_db, capsys):
    db.select(["INVALID", "QUERY"])
    captured = capsys.readouterr()
    assert "Unsupported query format." in captured.out