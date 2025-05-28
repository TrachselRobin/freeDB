# FreeDB Technical Documentation

## Overview

**FreeDB** is a lightweight, file-based database management system written in Python. It provides basic database operations such as creating databases and tables, inserting, updating, deleting, and querying data using a simple command interface. Data is stored in CSV files, making it easy to inspect and manipulate outside the system if needed.

---

## Features

- Create and switch between databases
- Create tables with custom columns
- Insert, update, and delete records
- Query data with `SELECT`, `WHERE`, and `LIKE` support
- Alter tables to add columns
- Configuration of data storage path
- Simple CLI and Python API

---

## Usage

### Installation

```bash
pip install .
```

### CLI Usage

Run commands using:

```bash
python -m freedb <command> [args...]
```

#### Example Commands

- **Configure data path:**
  ```
  python -m freedb config path <directory>
  ```

- **Create a database:**
  ```
  python -m freedb create database <dbname>
  ```

- **Switch database:**
  ```
  python -m freedb use <dbname>
  ```

- **Create a table:**
  ```
  python -m freedb create table <tablename> columns <col1> <col2> ...
  ```

- **Insert data:**
  ```
  python -m freedb insert <tablename> values <val1> <val2> ...
  ```

- **Select all:**
  ```
  python -m freedb read SELECT * FROM <tablename>
  ```

- **Select with WHERE:**
  ```
  python -m freedb read SELECT * FROM <tablename> WHERE <col>=<val>
  ```

- **Select with LIKE:**
  ```
  python -m freedb read SELECT * FROM <tablename> LIKE '<pattern>'
  ```

- **Update:**
  ```
  python -m freedb update <tablename> set <col>=<val> where <col>=<val>
  ```

- **Delete table:**
  ```
  python -m freedb delete table <tablename>
  ```

---

## Python API

You can also use FreeDB as a Python module:

```python
import freedb as db

db.create_database("mydb")
db.use("mydb")
db.create_table("users", ["id", "name", "email"])
db.insert(["users", "values", "1", "Alice", "alice@example.com"])
db.select(["SELECT", "*", "FROM", "users"])
```

---

## Data Storage

- Each database is a directory under the configured data path.
- Each table consists of two CSV files:
  - `<dbname>.<tablename>.structure.csv` — stores column headers
  - `<dbname>.<tablename>.content.csv` — stores the actual data

---

## Configuration

- The data directory and current database are stored in `freedb_config.json`.
- Use `python -m freedb config path <directory>` to change the data directory.

---

## Testing

Run all tests with:

```bash
pytest
```

---

## Extending

- Add new commands by creating a new Python file in `freedb/commands/` and importing it in `freedb/commands/__init__.py`.
- Follow the pattern of existing commands for argument parsing and file operations.

