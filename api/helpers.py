def validate_person(name):
    return True

def validate_account(currency, balance, person_id):
    if not validate_currency(currency):
        return False
    if balance <= 0:
        return False
    
    return True

def validate_transaction(currency, amount, sender_id, recipient_id):
    if not validate_currency(currency):
        return False
    if amount <= 0:
        return False
    
    return True


def validate_currency(currency):
    return (currency in ['USD', 'RUB', 'EUR'])