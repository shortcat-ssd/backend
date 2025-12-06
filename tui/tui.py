import utils
from client import APIClient
import getpass

def login(client):
    print("""
    
========= Login ========= 
    """)
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()

    if not utils.validate_username(username) or not utils.validate_password(password):
        login(client)

    response = client.login(username, password)

    if response.status_code == 200:
        print("Login effettuato con successo!\n")
    else:
        print("Errore nel login:", response.text)
        exit(1)



def menu(client):
    while True:
        print("""
        
*********** Shortcat TUI ************ 

    1) Lista URL accorciati
    2) Crea nuovo short
    3) Visualizza dettagli short
    4) Elimina uno short
    5) Mostra click di uno short
    6) Esci
    
**************************************
                    """)

        choice = input("> ").strip()

        if choice == "1":
            r = client.list_shorts()
            print(r.json())

        elif choice == "2":
            url = input("Inserisci URL: ").strip()
            #if validate_url(url):
             #   r = client.create_short(url)
              #  print(r.json())

        elif choice == "3":
            code = input("Inserisci codice shortcut: ")
            r = client.get_short(code)
            print(r.json())

        elif choice == "4":
            code = input("Inserisci codice shortcut da eliminare: ")
            r = client.delete_short(code)
            print("Eliminato" if r.status_code == 204 else r.text)

        elif choice == "5":
            code = input("Inserisci codice shortcut: ")
            r = client.list_clicks(code)
            print(r.json())

        elif choice == "6":
            print("Uscita...")
            break

        else:
            print("Scelta non valida.")




def main():
    client = APIClient("http://localhost:8000")
    login(client)
    menu(client)


if __name__ == "__main__":
    main()