from .models import Person, Account
from api import db

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
        person=Person.query.get(id)
        print([[u[0].__dict__['id'], u[0].__dict__['currency'], u[0].__dict__['balance'], u[0].__dict__['person_id']] for u in db.session.execute(person.accounts)])
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


def listAccounts_resolver(obj, info):
    try:
        accounts = [account.to_dict() for account in Account.query.all()]
        print(accounts)
        payload = {
            "success": True,
            "accounts": accounts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def getAccount_resolver(obj, info, id):
    try:
        account =Account.query.get(id)
        print(account)
        payload = {
            "success": True,
            "account": account.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload