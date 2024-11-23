from api import app, db
import datetime
import random
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify, session, redirect, url_for, make_response
from flask_cors import cross_origin
from api.insertdata import insertPerson
from api.queries import listPersons_resolver, getPerson_resolver, listAccounts_resolver, getAccount_resolver, getTransaction_resolver, listTransactions_resolver
from api.mutations import create_person_resolver, create_account_resolver, create_transaction_resolver

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/graphql", methods=["GET"])
@cross_origin(origins='http://127.0.0.1:5000', supports_credentials=True, headers=["Cookie"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
@cross_origin(origins='http://127.0.0.1:5000', supports_credentials=True, headers=["Cookie"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=[request, request.cookies.get('id')],
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route('/setcookie', methods=["GET"])
def set_cookie():
    response = make_response("Cookie has been set!")
    if not request.args.get('id'):
        response.set_cookie('id', str(random.randint(1, 1000)), domain='127.0.0.1', httponly = True)
    else:
        response.set_cookie('id', str(request.args.get('id')), domain='127.0.0.1', httponly = True)
    return response

@app.route('/getcookie')
def get_cookie():
    cookie_value = request.cookies.get('id')
    return str(cookie_value)

def prepare_schema_configuration():
    global query, mutation, type_defs, schema

    query = ObjectType("Query")
    mutation = ObjectType("Mutation")

    query.set_field("listPersons", listPersons_resolver)
    query.set_field("getPerson", getPerson_resolver)
    mutation.set_field("createPerson", create_person_resolver)


    query.set_field("listAccounts", listAccounts_resolver)
    query.set_field("getAccount", getAccount_resolver)
    mutation.set_field("createAccount", create_account_resolver)

    query.set_field("listTransactions", listTransactions_resolver)
    query.set_field("getTransaction", getTransaction_resolver)
    mutation.set_field("createTransaction", create_transaction_resolver)

    type_defs = load_schema_from_path("schema.graphql")
    schema = make_executable_schema(type_defs, [query, mutation]) 


with app.app_context():
    db.create_all()

    #insertPerson()

    prepare_schema_configuration()      