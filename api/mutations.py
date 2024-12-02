from api import db
from api.models import Person, Account, Transaction
from api.auth import authorization_person, authorization_account
from api.helpers import validate_person, validate_account, validate_transaction

def create_person_resolver(obj, info, name):
    try:
        status = validate_person(name)
        if not status:
            return {
                "success": False,
                "errors": ['Validate error']
            }
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
        status = validate_account(currency, balance, person_id)
        if not status:
            return {
                "success": False,
                "errors": ['Validate error']
            }

        status = authorization_person(info, person_id)
        if not status:
            return {
                "success": False,
                "errors": ['Forbidden']
            }
        account = Account(
            currency=currency,
            balance=balance,
            person_id=person_id
        )
        db.session.add(account)
        db.session.commit()
        payload = {
            "success": True,
            "account": account.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect parametres"]
        }
    return payload

def create_transaction_resolver(obj, info, currency, amount, sender_id, recipient_id):
    try: 
        status = validate_transaction(currency, amount, sender_id, recipient_id)
        if not status:
            return {
                "success": False,
                "errors": ['Validate error']
            }
        
        status = authorization_account(info, sender_id)
        if not status:
            return {
                "success": False,
                "errors": ['Forbidden']
            }

        account = Account.query.get(int(sender_id))
        if account.to_dict()['currency'] == currency or ((currency == "USD") and (account.to_dict()['currency'] == "EUR")) or ((currency == "EUR") and (account.to_dict()['currency'] == "USD")):

            if int(account.to_dict()['balance']) < amount:
                return {
                    "success": False,
                    "errors": ['Not enough balance']
                }
            
            account.balance = int(account.to_dict()['balance']) - amount

        elif currency == "USD" or currency == "EUR":

            if int(account.to_dict()['balance']) < amount * 100:
                return {
                    "success": False,
                    "errors": ['Not enough balance']
                }
            
            account.balance = int(account.to_dict()['balance']) - amount * 100

        elif currency == "RUB":

            if int(account.to_dict()['balance']) < (amount / 100):
                return {
                    "success": False,
                    "errors": ['Not enough balance']
                }
            
            account.balance = int(account.to_dict()['balance']) - amount / 100
        
        recipient = Account.query.get(int(recipient_id))
        if currency == recipient.to_dict()['currency'] or ((currency == "USD") and (recipient.to_dict()['currency'] == "EUR")) or ((currency == "EUR") and (recipient.to_dict()['currency'] == "USD")):
            recipient.balance = int(recipient.to_dict()['balance']) + amount
        elif currency == "USD" or currency == "EUR":
            recipient.balance = int(recipient.to_dict()['balance']) + amount * 100
        elif currency == "RUB":
            recipient.balance = int(recipient.to_dict()['balance']) + amount / 100

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