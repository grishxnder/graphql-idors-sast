from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    accounts = db.relationship('Account', backref='person', lazy='dynamic')
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "accounts": [account.to_dict() for account in self.accounts]
        }

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String)
    balance = db.Column(db.Integer)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    transactions_sender = db.relationship('Transaction', foreign_keys='Transaction.sender_id', backref='sender', lazy='dynamic')
    transactions_receiver = db.relationship('Transaction', foreign_keys='Transaction.recipient_id', backref='recipient', lazy='dynamic')

    def to_dict(self):
        return {
            "id": self.id,
            "currency": self.currency,
            "balance": self.balance,
            "person_id": self.person_id,
            "transactions": [transaction.to_dict() for transaction in self.transactions_sender],
        }
    

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String)
    amount = db.Column(db.Integer)
    sender_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    def to_dict(self):
        return {
            "id": self.id,
            "currency": self.currency,
            "amount": self.amount,
            "sender_id": self.sender_id,
            "recipient_id": self.recipient_id
        }