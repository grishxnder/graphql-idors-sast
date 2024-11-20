from api import db
from api.models import Person, Account, Transaction

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

def create_transaction_resolver(obj, info, currency, amount, sender_id, recipient_id):
    try:
        transaction = Transaction(
            currency=currency,
            amount=amount,
            sender_id=sender_id,
            recipient_id=recipient_id
        )
        db.session.add(transaction)
        db.session.commit()
        payload = {
            "success": True,
            "transaction": transaction.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect parametres"]
        }
    return payload