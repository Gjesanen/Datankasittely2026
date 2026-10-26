from dataprotection.pseudonymization import pseudonymize_names, restore_names
from dataprotection.anonymization import anonymize
from dataprotection.masking import mask


def demo_pseudonymization():
    names = [
        "Matti Meikäläinen",
        "Liisa Laulaja",
        "Juha Jokunen",
        "Seppo Selkonen",
        "Hubert Huilu",
        "Alice Wonderland",
        "Bob Builder",
        "Charlie Chaplin",
    ]
    encrypted = pseudonymize_names(names)
    restored = restore_names(encrypted)

    print("Original:", names)
    print("Encrypted:", encrypted)
    print("Restored:", restored)


def demo_anonymization():
    people = [
        {"name": "Matti Meikäläinen", "birthdate": "1990-05-15", "city": "Helsinki"},
        {"name": "Liisa Laulaja", "birthdate": "1985-12-12", "city": "Tampere"},
        {"name": "Juha Jokunen", "birthdate": "1978-01-30", "city": "Oulu"},
        {"name": "Seppo Selkonen", "birthdate": "2001-09-22", "city": "Turku"},
        {"name": "Alice Wonderland", "birthdate": "1995-07-07", "city": "London"},
        {"name": "Bob Builder", "birthdate": "1980-03-14", "city": "Berlin"},
    ]
    print("Anonymized:", anonymize(people))

    """
    Expected
    [
        {"birth_year": 1990, "city_initial": "H"},
        etc.
    ]
    """


def demo_masking():
    people = [
        {"name": "Matti Meikäläinen", "email": "matti.meikalainen@example.com", "phone": "0501234567"},
        {"name": "Liisa Laulaja", "email": "liisa.laulaja@example.org", "phone": "0407654321"},
        {"name": "Juha Jokunen", "email": "juha.jokunen@work.fi", "phone": "0441112223"},
        {"name": "Seppo Selkonen", "email": "seppo.s@example.com", "phone": "0469998887"},
        {"name": "Alice Wonderland", "email": "alice@wonderland.net", "phone": "1234567890"},
    ]
    print("Masked:", mask(people))

    """
    Expected 
    [
        {"name": "Matti Meikäläinen", "email": "*******************@example.com", "phone": "********67"},
        etc.
    ]
    """


if __name__ == "__main__":
    demo_pseudonymization()
    demo_anonymization()
    demo_masking()