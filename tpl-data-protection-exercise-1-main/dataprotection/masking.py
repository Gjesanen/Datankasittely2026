def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """

    masked_people = []

    for person in people:
        email = person.get("email")
        phone = person.get("phone")
        masked_person = dict(person)
        masked_person["email"] = (
            email.split("@")[0][0] + "***@" + email.split("@")[1]
        )
        masked_person["phone"] = (
            "*" * (len(phone) - 2) + phone[-2:]
        )
        masked_people.append(masked_person)

    return masked_people