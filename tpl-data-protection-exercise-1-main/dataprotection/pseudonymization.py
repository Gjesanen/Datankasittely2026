from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""
key = Fernet.generate_key()
cipher = Fernet(key)

def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """

    return [cipher.encrypt(name.encode()).decode() for name in names]


def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """

    return [cipher.decrypt(enc.encode()).decode() for enc in encrypted]