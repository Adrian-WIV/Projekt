#imports
import tkinter as tk
from tkinter import ttk, messagebox
#import für Bilder
import os

#Fenster erstellen
root = tk.Tk()
root.title ("Suchprogramm")
root.geometry("1050x600")

#Eingabefelder
labels = ["ID:", "Vorname:", "Nachname:", "Produkte:"]
inputs = {} #Alle Eingabefelder gesammelt nach Namen

#Geht alle Feldnamen durch
for i, label in enumerate(labels):
    #Zeigt den Text (ID, Name, etc.) links im Fenster an
    tk.Label(root, text=label).place(x=20, y=30 + i * 40)  #Position: 20 Pixel von links, und 40 Pixel nach unten versetzt

    eingabe = tk.Entry(root)  #Erstellt ein Textfeld
    eingabe.place(x=120, y=30 + i * 40, width=180)  #Position des Textfelds rechts neben dem Label
    inputs[label.strip(":")] = eingabe  #Speichert das Textfeld ohne Doppelpunkt

#Monat-Auswahl als Dropdown
tk.Label(root, text="Monat:").place(x=20, y=30 + len(labels) * 40)
monat_combo = ttk.Combobox(root, values=[
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
])
monat_combo.place(x=120, y=30 + len(labels) * 40, width=180)
inputs["Monat"] = monat_combo

#Jahr-Auswahl als Dropdown
tk.Label(root, text="Jahr:").place(x=20, y=30 + (len(labels) + 1) * 40)
jahr_combo = ttk.Combobox(root, values=["2024", "2025"])
jahr_combo.place(x=120, y=30 + (len(labels) + 1) * 40, width=180)
inputs["Jahr"] = jahr_combo

#Spaltenüberschriften der Tabelle
columns = ("ID", "Vorname", "Nachname", "Produkte", "Menge", "Monat", "Jahr")

#### Beispiel-Daten ####
daten = [
    (1, "Adrian", "Badar", "Gabelstapler P", 2, "April", "2024"),
    ("", "", "", "Gabelstapler W", 1, "April", "2024"),
    (2, "Lucas", "Lehmeyer", "Ameise ;)", 3, "Mai", "2025")
]

#Such-Button
def suchen():
    suchkriterien = {}  #Hier werden alle eingegebenen Suchwerte gespeichert

    #Geht alle Eingabefelder durch
    for feldname, eingabe in inputs.items():
        inhalt = eingabe.get().strip()  #Holt den eingegebenen Text und entfernt Leerzeichen
        if inhalt:  #Wenn etwas eingegeben wurde
            suchkriterien[feldname] = inhalt  #Speichert den Text unter dem passenden Namen (z. B. "ID")

    #Prüft, ob die ID nur aus Zahlen besteht
    if "ID" in suchkriterien:
        if not suchkriterien["ID"].isdigit():
            messagebox.showerror("Fehler", "ID muss eine Zahl sein.")
            return  #Abbruchbedingung: wenn ID ungültig ist

    #Prüft, ob der Monat gültig ist
    gültige_monate = [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ]
    if "Monat" in suchkriterien:
        if suchkriterien["Monat"] not in gültige_monate:
            messagebox.showerror("Fehler", "Ungültiger Monat eingegeben.")
            return  #Abbruchbedingung: wenn der Monat nicht erkannt wird

    #Prüft, ob das Jahr gültig ist
    if "Jahr" in suchkriterien:
        if suchkriterien["Jahr"] not in ["2024", "2025"]:
            messagebox.showerror("Fehler", "Ungültiges Jahr eingegeben.")
            return  #Abbruchbedingung: wenn das Jahr nicht erkannt wird

    #Tabelle leeren
    for zeile in tabelle.get_children():
        tabelle.delete(zeile)

    #Daten durchsuchen
    for datensatz in daten:
        match = True  #Passt Zeile zu Suchkriterien?

        #Verbindet Spaltennamen mit Werten der aktuellen Zeile
        datensatz_dict = dict(zip(columns, datensatz))

        #Geht alle eingegebenen Suchkriterien durch
        for feldname, inhalt in suchkriterien.items():
            feldwert = str(datensatz_dict.get(feldname, "")).lower()  #Wert in der Zeile
            eingabe = inhalt.lower()  #Suchtext

            #Wird auf genaue Übereinstimmung geprüft
            if feldname == "ID":
                if feldwert != eingabe:
                    match = False
                    break
            else:
                #Bei allen anderen Feldern reicht Teilwort
                if eingabe not in feldwert:
                    match = False
                    break

        if match:     #Wenn Zeile passt, wird sie in die Tabelle eingefügt
            tabelle.insert("", tk.END, values=datensatz)

#Such-Button, der die Funktion "suchen" aufruft
such_btn = tk.Button(root, text="Suchen", command=suchen)
such_btn.place(x=120, y=30 + (len(labels) + 2) * 40, width=180)

#Rahmen für die Tabelle
tabelle_frame = tk.Frame(root)
tabelle_frame.place(x=350, y=20, width=670, height=440)

#Scrollleisten für die Tabelle
scroll_y = tk.Scrollbar(tabelle_frame, orient=tk.VERTICAL)
scroll_x = tk.Scrollbar(tabelle_frame, orient=tk.HORIZONTAL)

#Tabelle erstellen
tabelle = ttk.Treeview(tabelle_frame, columns=columns, show="headings",
                       yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

#Scrollleisten mit der Tabelle verbinden
scroll_y.config(command=tabelle.yview)
scroll_x.config(command=tabelle.xview)

#Scrollleisten und Tabelle im Fenster anzeigen
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
tabelle.pack(fill=tk.BOTH, expand=True)

#Spaltenbreiten
spaltenbreiten = [40, 80, 100, 150, 60, 80, 60]

#Spaltenüberschriften setzen und zentrieren
for index, spaltenname in enumerate(columns):
    tabelle.heading(spaltenname, text=spaltenname, anchor="center")  #Text oben in der Spalte
    tabelle.column(spaltenname, width=spaltenbreiten[index], anchor="center")  #Spaltenbreite + Ausrichtung

#Fügt alle Beispiel-Daten in die Tabelle ein (Monat/Jahr nur bei neuer Bestellung)
letzte_id = None  #Merkt sich die letzte ID
for datensatz in daten:
    aktuelle_id = datensatz[0]

    #Wenn ID leer oder gleich wie vorher: Monat und Jahr ausblenden
    if aktuelle_id == "" or aktuelle_id == letzte_id:
        datensatz_angepasst = list(datensatz)
        datensatz_angepasst[5] = ""  # Monat leeren
        datensatz_angepasst[6] = ""  # Jahr leeren
        tabelle.insert("", tk.END, values=datensatz_angepasst)
    else:
        tabelle.insert("", tk.END, values=datensatz)
        letzte_id = aktuelle_id

#Badmeyer-Logo unten links
try:
    bildpfad = "badmeyer_small.png"  #Pfad zur Bilddatei

    #Prüft, ob die Bilddatei existiert
    if not os.path.isfile(bildpfad):
        raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")

    #Bild laden
    logo_bild = tk.PhotoImage(file=bildpfad)

    #Bild ggf. verkleinern oder vergrößern
    logo_bild = logo_bild.subsample(1, 1)

    #Bild in einem Label anzeigen
    logo_label = tk.Label(root, image=logo_bild, bg=root.cget("bg"))
    logo_label.image = logo_bild  # Verhindert, dass das Bild aus dem Speicher verschwindet
    logo_label.place(x=60, y=320)  # Position des Bildes unten links

#Falls beim Laden etwas schiefläuft, Ausgabe im Terminal
except Exception as fehler:
    print("Fehler beim Laden des Bildes:", fehler)
    print("Aktueller Pfad:", os.getcwd())
    print("Dateien im Ordner:", os.listdir())

#Anwendung wird gestartet
root.mainloop()
