from .models import Person, Account, Transaction
from flask import request, jsonify, session, redirect, url_for
from api import db
from api.auth import authorization_person, authorization_account, authorization_transaction

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
        status = authorization_person(info, id)
        if not status:
            return {
                "success": False,
                "errors": ['Forbidden']
            }
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
        status = authorization_account(info, id)
        if not status:
            return {
                "success": False,
                "errors": ['Forbidden']
            }
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
        status = authorization_transaction(info, id)
        if not status:
            return {
                "success": False,
                "errors": ['Forbidden']
            }
        transaction=Transaction.query.get(id)
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