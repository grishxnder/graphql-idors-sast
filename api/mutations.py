from datetime import date

from api import db
from api.models import Person

def create_person_resolver(obj, info, name):
    try:
        person = Person(
            name=name
        )
        db.session.add(person)
        db.session.commit()
        payload = {
            "success": True,
            "person": person.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload