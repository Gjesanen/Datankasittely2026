import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dataprotection.anonymization import anonymize

def test_anonymization():
    people = [
        {"name": "Alice Example", "birthdate": "1992-08-01", "city": "London"}
    ]
    result = anonymize(people)
    assert result == [{"birth_year": 1992, "city_initial": "L"}]