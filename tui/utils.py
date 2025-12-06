from urllib.parse import urlparse

def validate_username(username: str) -> bool:
    if not username or not username.strip():
        print("Username non può essere vuoto")
        return False
    return True

def validate_password(password: str) -> bool:

    if not password or not password.strip():
        print("Errore: la password non può essere vuota.")
        return False

#    if len(password) < 6:
#        print("Errore: la password deve essere lunga almeno 6 caratteri.")
#       return False

    if not any(c.isdigit() for c in password):
        print("Errore: la password deve contenere almeno un numero.")
        return False

    if not any(c.isalpha() for c in password):
        print("Errore: la password deve contenere almeno una lettera.")
        return False

    return True


