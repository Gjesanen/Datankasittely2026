import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dataprotection.pseudonymization import pseudonymize_names, restore_names

def test_roundtrip():
    names = ["Alice Example", "Bob Test"]
    encrypted = pseudonymize_names(names)
    restored = restore_names(encrypted)
    assert restored == names