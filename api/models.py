from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }