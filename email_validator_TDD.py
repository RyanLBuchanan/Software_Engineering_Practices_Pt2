def email_validator(email):
    if email.count('@') != 0 and email.count('.') != 0:
        return True
    else:
        return False

email_validator('ryan@gmail.com')
