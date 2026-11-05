from data_protection.masking import update_users_with_masked_phones
from data_protection.anonymization import update_users_with_anonymized_names

print("Starting data protection...")
print("=" * 80)


update_users_with_masked_phones()


update_users_with_anonymized_names()
