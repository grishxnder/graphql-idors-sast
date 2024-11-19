from api import db
from api.models import Person, Account

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
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect name"]
        }
    return payload

def create_account_resolver(obj, info, currency, balance, person_id):
    try:
        account = Account(
            currency=currency,
            balance=balance,
            person_id=person_id
        )
        db.session.add(account)
        db.session.commit()
        payload = {
            "success": True,
            "person": account.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect parametres"]
        }
    return payload