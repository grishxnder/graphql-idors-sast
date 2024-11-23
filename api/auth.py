from .models import Person, Account, Transaction
from api import db

def authorization_person(context, requestId):
    clientId = int(context[10][1])
    if int(clientId) != int(requestId):
        return False
    else:
        return True

def authorization_account(context, requestId):
    clientId = int(context[10][1])
    accounts = get_accounts(clientId)

    return any([(int(account['id']) == int(requestId)) for account in accounts])
    
def authorization_transaction(context, requestId):
    clientId = int(context[10][1])
    clientId = int(context[10][1])
    person = Person.query.get(clientId)
    accounts = person.to_dict()['accounts']


    for account in accounts:
        for transaction in account['transactions']:
            if int(transaction['id']) == int(requestId):
                   return True
    return False


def get_accounts(person_id):
    person = Person.query.get(person_id)
    accounts = person.to_dict()['accounts']
    return accounts

def get_transactions(person_id):
    person = Person.query.get(person_id)
    accounts = person.to_dict()['accounts']
    return accounts