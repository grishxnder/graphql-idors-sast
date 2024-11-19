from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    accounts = db.relationship('Account', backref='person', lazy='dynamic')
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "accounts": self.accounts
        }

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String)
    balance = db.Column(db.Integer)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    def to_dict(self):
        return {
            "id": self.id,
            "currency": self.currency,
            "balance": self.balance,
            "person_id": self.person_id
        }