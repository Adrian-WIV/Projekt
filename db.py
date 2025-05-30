#imports

import mariadb
import sys

#Klassen

class Kunden():
    def __init__(self, vorname, name, straße, hausnummer, plz, tel, geb, email):
        self.vorname = vorname
        self.name = name
        self.straße = straße
        self.hausnummer = hausnummer
        self.plz = plz
        self.tel = tel
        self.geb = geb
        self.email = email


#connect mariadb
def mariadbconnect():
    try: 
        conn = mariadb.connect(
            user = "Adrian",
            password = "Passwort",
            host = "localhost",
            port = 3306,
            database = "schlumpfshop3"
        )

        print("verbindung erfolgreich")
    
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")

    cur = conn.cursor()

    return cur, conn

def kundenliste(cur, eingabe):
    cur.execute("""xx""")
    ergebnis = cur.fetchall()

    kunden_liste = []

    for e in ergebnis:
        kunde = Kunden(*e)
        kunden_liste.append(kunde)

    return kunden_liste

def sql_einzelansicht(id="", vorname="", nachname="", produkte="", menge="", monat="", jahr=""):
    conn = mariadbconnect()
    cur = conn.cursor()

    abfrage = """ SELECT  """