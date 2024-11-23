from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000", "supports_credentials": True}})
app.config['CORS_HEADERS'] = 'Content-Type'


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123@127.0.0.1:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    result = db.session.query(db.text('version()')).all()
    answer = '<h1> It seems, that all works OK. </h1> <p> <b> DB Version is: </b>' + str(result[0][0]) + '</p>'
    return answer   