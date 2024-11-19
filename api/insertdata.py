from api import db, app
from api.models import Person


def insertPerson():
    with app.app_context():
        new_person = Person(name="Test User")
        db.session.add(new_person)
        db.session.commit()
        print("Person added", str(new_person))