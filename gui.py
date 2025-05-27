#imports
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
#import für Bilder
import os
#Variablen
inputs = {}

#Fenster erstellen
root = ThemedTk(theme="winxpblue")
root.title ("Badmeyer")
root.geometry("950x500")

main_frame = ttk.Frame(root)
main_frame.place(x=0, y=0, relwidth=1, relheight=1)

einzel_frame = ttk.Frame(main_frame)
gesamt_frame = ttk.Frame(main_frame)

#bild global laden

try:
    bildpfad = "badmeyer_small-removebg.png"
    if not os.path.isfile(bildpfad):
        raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")
    logo_bild = tk.PhotoImage(file=bildpfad)
except Exception as fehler:
    print("Fehler beim Laden des Bildes:", fehler)
    logo_bild = None  

#Funktionen
#Frame auswahl
def zeige_frame(frame):
    
    for unterframe in main_frame.winfo_children():
        unterframe.place_forget()
    frame.place(x=0, y=0, relwidth=1, relheight=1)


def einzelsuche():
    ##################

    #Eingabefelder
        labels = ["ID:", "Vorname:", "Nachname:", "Produkte:"]
        inputs.clear()

        #Geht alle Feldnamen durch
        for i, label in enumerate(labels):
            #Zeigt den Text (ID, Name, etc.) links im Fenster an
            ttk.Label(einzel_frame, text=label).place(x=20, y=30 + i * 40)  #Position: 20 Pixel von links, und 40 Pixel nach unten versetzt

            #Bei "Monat" wird ein Dropdown/Combobox angezeigt
            if label == "Monat:":
                combo = ttk.Combobox(einzel_frame, values=[
                    "Januar", "Februar", "März", "April", "Mai", "Juni",
                    "Juli", "August", "September", "Oktober", "November", "Dezember"
                ])
                combo.place(x=120, y=30 + i * 40, width=180)  #Position der Auswahlliste
                inputs["Monat"] = combo  #Speichert die Auswahlliste unter dem Namen "Monat"

            else:
                eingabe = ttk.Entry(einzel_frame)  #Erstellt ein Textfeld
                eingabe.place(x=120, y=30 + i * 40, width=180)  #Position des Textfelds rechts neben dem Label
                inputs[label.strip(":")] = eingabe  #Speichert das Textfeld ohne Doppelpunkt

    #Monat-Auswahl als Dropdown
        tk.Label(einzel_frame, text="Monat:").place(x=20, y=30 + len(labels) * 40)
        monat_combo = ttk.Combobox(einzel_frame, values=[
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ])
        monat_combo.place(x=120, y=30 + len(labels) * 40, width=180)
        inputs["Monat"] = monat_combo

        #Jahr-Auswahl als Dropdown
        ttk.Label(einzel_frame, text="Jahr:").place(x=20, y=30 + (len(labels) + 1) * 40)
        jahr_combo = ttk.Combobox(einzel_frame, values=["2024", "2025"])
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
        such_btn = ttk.Button(einzel_frame, text="Suchen", command=suchen)
        such_btn.place(x=120, y=30 + (len(labels) + 2) * 40, width=180)

        #Rahmen für die Tabelle
        tabelle_frame = ttk.Frame(einzel_frame)
        tabelle_frame.place(x=350, y=20, width=670, height=440)

            #Scrollleisten für die Tabelle
        scroll_y = ttk.Scrollbar(tabelle_frame, orient=tk.VERTICAL)
        scroll_x = ttk.Scrollbar(tabelle_frame, orient=tk.HORIZONTAL)

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
            bildpfad = "badmeyer_small-removebg.png"  #Pfad zur Bilddatei

            #Prüft, ob die Bilddatei existiert
            if not os.path.isfile(bildpfad):
                raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")

            #Bild laden
            if logo_bild:
                logo_label = tk.Label(einzel_frame, image=logo_bild)
                logo_label.image = logo_bild
                logo_label.place(x=60, y=320)  # Position des Bildes unten links

        #Falls beim Laden etwas schiefläuft, Ausgabe im Terminal
        except Exception as fehler:
            print("Fehler beim Laden des Bildes:", fehler)
            print("Aktueller Pfad:", os.getcwd())
            print("Dateien im Ordner:", os.listdir())

    






def gesamtsuche():

    #Eingabefelder

    labels = ["Kunde:", "Produkt:"]
    gesamt_inputs = {}

    for i, label in enumerate(labels):
         ttk.Label(gesamt_frame, text=label).place(x=20,y=30 + i *40)
         eingabe = ttk.Entry(gesamt_frame)
         eingabe.place(x=120, y=30 + i *40, width=180)
         gesamt_inputs[label.strip(":")] = eingabe

    #Monate(Combobox)

    label_monat = ttk.Label(gesamt_frame, text="Monta:")
    label_monat.place(x=20, y=30 + len(labels) * 40)
    monat_combo = ttk.Combobox(gesamt_frame,values=[
         "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ])
    monat_combo.place(x=120, y=30 + len(labels) * 40, width=180)
    gesamt_inputs["Monat"] = monat_combo

    #Jahre(Combobox)

    combo_jahr = ttk.Label(gesamt_frame, text="Jahr:")
    combo_jahr.place(x=20, y=30 + (len(labels) + 1) * 40)
    jahr_combo = ttk.Combobox(gesamt_frame, values=["2024", "2025"])
    jahr_combo.place(x=120, y=30 + (len(labels) + 1) * 40, width=180)
    gesamt_inputs["Jahr"] = jahr_combo

    #Treeview für gesamtsuche()
    #Spalten
    spalten = ("Kunde", "Produkt", "Menge", "Monat", "Jahr")

    #TV und Scrollbar
    tabelle_frame = ttk.Frame(gesamt_frame)
    tabelle_frame.place(x=350, y=20, width=570, height=440)

    scroll_y = ttk.Scrollbar(tabelle_frame, orient=tk.VERTICAL)
    scroll_x = ttk.Scrollbar(tabelle_frame, orient=tk.HORIZONTAL)

    gesamt_tabelle = ttk.Treeview(tabelle_frame, columns=spalten, show="headings", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    scroll_y.config(command=gesamt_tabelle.yview)
    scroll_x.config(command=gesamt_tabelle.xview)

    scroll_y.pack(side= tk.RIGHT, fill=tk.Y)
    scroll_x.pack(side= tk.BOTTOM, fill=tk.X)
    gesamt_tabelle.pack(fill=tk.BOTH, expand=True)

    #breite überschrift

    spaltenbreiten = [40, 150, 60, 80, 60]

    for i, spalte in enumerate(spalten):
         gesamt_tabelle.heading(spalte, text= spalte, anchor="center")
         gesamt_tabelle.column(spalte, width=spaltenbreiten[i], anchor="center")

    gesamt_daten = [
         ("Firma Müller", "Gabelstapler P", 3, "April", "2024"),
        ("Firma Müller", "Gabelstapler W", 1, "April", "2024"),
        ("Firma Schmidt", "Ameise", 4, "Mai", "2025")
    ]

    #suche für gesamtansicht

    def gesamt_suche():
        suchkriterien = {}

        for feld, eingabe in gesamt_inputs.items():
            wert= eingabe.get().strip()
            if wert:
                 suchkriterien[feld] = wert.lower()
        
        #leeren
        for zeile in gesamt_tabelle.get_children():
             gesamt_tabelle.delete(zeile)
        
        #daten filtern

        for datensatz in gesamt_daten:
            datensatz_dict = dict(zip(spalten, datensatz))
            match=True
            for feld, wert in suchkriterien.items():
                  eintrag = str(datensatz_dict.get(feld, "")).lower()
                  if wert not in eintrag:
                       match = False
                       break
            if match:
                gesamt_tabelle.insert("", tk.END, values= datensatz)

    #suche button

    btn_suche = ttk.Button(gesamt_frame, text="Suchen", command= gesamtsuche)
    btn_suche.place(x=120, y=30 + (len(labels) + 2) *40, width=180)






    # Bild unten links
    try:
        bildpfad = "badmeyer_small-removebg.png"
        if not os.path.isfile(bildpfad):
            raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")
        if logo_bild:
            logo_label = tk.Label(gesamt_frame, image=logo_bild)
            logo_label.image = logo_bild
            logo_label.place(x=60, y=320)

    except Exception as fehler:
        print("Fehler beim Laden des Bildes (Gesamtsuche):", fehler)


#Menu Erstellen
my_menu = tk.Menu(root)
root.config(menu=my_menu)

my_menu.add_command(label="Einzelansicht", command= lambda: zeige_frame(einzel_frame))
my_menu.add_command(label="Gesamtsuche", command= lambda: zeige_frame(gesamt_frame))







# #Anwendung wird gestartet
einzelsuche()
gesamtsuche()
root.mainloop()
