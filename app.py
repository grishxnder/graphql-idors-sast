from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.insertdata import insertPerson
from api.queries import listPersons_resolver, getPerson_resolver, listAccounts_resolver, getAccount_resolver
from api.mutations import create_person_resolver, create_account_resolver

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


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

    type_defs = load_schema_from_path("schema.graphql")
    schema = make_executable_schema(type_defs, [query, mutation]) 


with app.app_context():
    db.create_all()

    #insertPerson()

    prepare_schema_configuration()