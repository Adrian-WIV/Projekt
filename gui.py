#imports
import tkinter as tk
from tkinter import ttk, messagebox
#import für Bilder
import os

#Fenster erstellen
root = tk.Tk()
root.title ("Suchprogramm")
root.geometry("950x500")

#Eingabefelder
labels = ["ID:", "Vorname:", "Nachname:", "Produkte:", "Monat:"]
inputs = {} #Alle Eingabefelder gesammelt nach Namen

#Geht alle Feldnamen durch
for i, label in enumerate(labels):
    #Zeigt den Text (ID, Name, etc.) links im Fenster an
    tk.Label(root, text=label).place(x=20, y=30 + i * 40)  #Position: 20 Pixel von links, und 40 Pixel nach unten versetzt

    #Bei "Monat" wird ein Dropdown/Combobox angezeigt
    if label == "Monat:":
        combo = ttk.Combobox(root, values=[
            "Januar", "Februar", "März", "April", "Mai", "Juni",
            "Juli", "August", "September", "Oktober", "November", "Dezember"
        ])
        combo.place(x=120, y=30 + i * 40, width=180)  #Position der Auswahlliste
        inputs["Monat"] = combo  #Speichert die Auswahlliste unter dem Namen "Monat"

    else:
        eingabe = tk.Entry(root)  #Erstellt ein Textfeld
        eingabe.place(x=120, y=30 + i * 40, width=180)  #Position des Textfelds rechts neben dem Label
        inputs[label.strip(":")] = eingabe  #Speichert das Textfeld ohne Doppelpunkt


#Spaltenüberschriften der Tabelle
columns = ("ID", "Vorname", "Nachname", "Produkte", "Menge", "Monat")

#### Beispiel-Daten ####
daten = [
    (1, "Adrian", "Badar", "Gabelstapler P", 2, "April"),
    ("", "", "", "Gabelstapler W", 1, ""),
    (2, "Lucas", "Lehmeyer", "Ameise ;)", 3, "Mai")
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
    if "Monat" in suchkriterien:
        gültige_monate = [
            "Januar", "Februar", "März", "April", "Mai", "Juni",
            "Juli", "August", "September", "Oktober", "November", "Dezember"
        ]
        if suchkriterien["Monat"] not in gültige_monate:
            messagebox.showerror("Fehler", "Ungültiger Monat eingegeben.")
            return  #Abbruchbedingung: wenn der Monat nicht erkannt wird