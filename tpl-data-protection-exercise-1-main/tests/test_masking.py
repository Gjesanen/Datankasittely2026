import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dataprotection.masking import mask

def test_masking():
    people = [
        {"name": "Alice Example", "email": "alice@example.com", "phone": "0501234567"}
    ]
    result = mask(people)[0]
    assert result["name"] == "Alice Example"
    assert result["email"].endswith("@example.com")
    assert result["phone"].endswith("67")