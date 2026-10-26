from datetime import datetime

def anonymize(people):
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """

    anonymized_people = []
    
    for person in people:
        anonymized_person = {
            "birth_year": datetime.strptime(person["birthdate"], "%Y-%m-%d").year,
            "city_initial": person["city"][0] if person.get("city") else None,
        }

        anonymized_people.append(anonymized_person)

    return anonymized_people
