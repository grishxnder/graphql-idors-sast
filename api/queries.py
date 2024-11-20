from .models import Person, Account, Transaction
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


def listTransactions_resolver(obj, info):
    try:
        transactions = [trans.to_dict() for trans in Transaction.query.all()]
        print(transactions)
        payload = {
            "success": True,
            "transactions": transactions
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getTransaction_resolver(obj, info, id):
    try:
        transaction=Transaction.query.get(id)
        print(transaction)
        payload = {
            "success": True,
            "transaction": transaction.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload