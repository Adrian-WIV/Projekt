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
            database = "projekt2"
        )

        print("verbindung erfolgreich")
        cur = conn.cursor()
        return conn, cur
    
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")

        return None, None

def kundenliste(cur, eingabe):
    cur.execute("""xx""")
    ergebnis = cur.fetchall()

    kunden_liste = []

    for e in ergebnis:
        kunde = Kunden(*e)
        kunden_liste.append(kunde)

    return kunden_liste

def sql_einzelansicht(id="", vorname="", nachname="", produkt="", menge="", monat="", jahr=""):
    conn, cur = mariadbconnect()
    if conn is None or cur is None:
        print("Keine Verbindung möglich")
        return []

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
        abfrage += " AND kunden.vorname LIKE ?"
        ausgabe.append(f"%{vorname}%")
    
    if nachname:
        abfrage += " AND kunden.name LIKE ?"
        ausgabe.append(f"%{nachname}%")

    if produkt:
        abfrage += " AND produkte.produktname LIKE ?"
        ausgabe.append(f"%{produkt}%")

    if monat:
        abfrage += " AND MONTH(bestellungen.bestelldatum) ?"
        ausgabe.append(int(monat))

    if jahr:
        abfrage += " AND YEAR(bestellungen.bestelldatum) ?"
        ausgabe.append(int(jahr))

    cur.execute(abfrage, tuple(ausgabe))
    daten = cur.fetchall()
    cur.close()
    conn.close()
    return daten

def sql_gesamtsuche(kunden_id="", produkt="", monat=None, jahr=None):
    conn, cur = mariadbconnect()
    if conn is None or cur is None:
        print("Keine Verbindung möglich")
        return []
    

    abfrage = """SELECT 
            kunden.IDKunde,
            kunden.Vorname,
            kunden.Name,
            produkte.Produktname,
            SUM(bestellposition.Menge) AS Gesamtmenge,
            SUM(bestellposition.Menge * bestellposition.Preis) AS Gesamtumsatz
        FROM kunden 
        JOIN bestellungen ON kunden.IDKunde = bestellungen.`kunden-id`
        JOIN bestellposition ON bestellungen.`Bestell-ID` = bestellposition.Bestell_ID
        JOIN produkte ON bestellposition.Produkt_ID = produkte.`Produkt-ID`
        WHERE 1=1
        """
    
    werte = []

    if kunden_id:
        abfrage += " AND kunden.IDKunde = ?"
        werte.append(kunden_id)

    if produkt:
        abfrage += " AND produkte.Produktname LIKE ?"
        werte.append(f"%{produkt}%")

    if monat and jahr:
        abfrage += " AND b.Bestelldatum >= STR_TO_DATE(CONCAT(?, '-', '01'), '%Y-%m-%d')"
        werte.append(f"{jahr}-{monat:02d}")
    elif jahr:
        abfrage += " AND YEAR(b.Bestelldatum) = ?"
        werte.append(jahr)
    elif monat:
        abfrage += " AND MONTH(b.Bestelldatum) = ?"
        werte.append(monat)

    abfrage += """
    GROUP BY kunden.IDKunde, kunden.Vorname, kunden.Name, produkte.Produktname
    ORDER BY kunden.IDKunde, produkte.Produktname
    """

    cur.execute(abfrage, tuple(werte))
    daten = cur.fetchall()
    conn.close()
    return daten