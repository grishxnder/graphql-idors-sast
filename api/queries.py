from .models import Person
def listPersons_resolver(obj, info):
    try:
        persons = [person.to_dict() for person in Person.query.all()]
        payload = {
            "success": True,
            "persons": persons
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getPerson_resolver(obj, info, id):
    try:
        person =Person.query.get(id)
        payload = {
            "success": True,
            "person": person.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload