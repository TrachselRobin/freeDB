import freedb as db
import sys
from io import StringIO

def test_create_output():
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    try:
        db.create()
        output = captured_output.getvalue()
        assert "Creating a new database entry..." in output
    finally:
        sys.stdout = old_stdout
    
    print("Test passed!")

if __name__ == "__main__":
    test_create_output()