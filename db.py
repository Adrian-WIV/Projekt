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

    abfrage = """ SELECT 
        kunden.IDKunde, 
        kunden.Vorname, 
        kunden.Name, 
        produkte.Produktname, 
        bestellposition.Menge, 
        MONTH(bestellungen.Bestelldatum) AS Monat, 
        YEAR(bestellungen.Bestelldatum) AS Jahr
    FROM kunden 
    JOIN bestellungen ON kunden.IDKunde = bestellungen.`kunden-id`
    JOIN bestellposition ON bestellungen.`Bestell-ID` = bestellposition.bestell_ID
    JOIN produkte ON bestellposition.Produkt_ID = produkte.`Produkt-ID`
    WHERE 1=1 """

    ausgabe = []

    if vorname:
        abfrage += "AND kunden.vorname LIKE ?"
        abfrage.append(f"%{vorname}%")
    
    if nachname:
        abfrage += "AND kunden.name LIKE ?"
        abfrage.append(f"%{nachname}%")

    if produkte:
        abfrage += "AND produkte.produktname LIKE ?"
        abfrage.append(f"%{produkte}%")

    if monat:
        abfrage += "AND MONTH(bestellungen.bestelldatum) LIKE ?"
        abfrage.append(f"%{int(monat)}%")

    if jahr:
        abfrage += " AND YEAR(bestellungen.bestelldatum) LIKE ?"
        abfrage.append(f"%{int(jahr)}%")

    cur.execute(abfrage, tuple(ausgabe))
    daten = cur.fetchall()
    conn.close()
    return daten