import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import os
import sys
from db import sql_einzelansicht, sql_gesamtsuche, do_login
import hashlib

# gemeinsames_passwort = "passwort"
# gehashter_pw = hashlib.sha256(gemeinsames_passwort.encode()).hexdigest()
# users = {"lucas": gehashter_pw, "adrian": gehashter_pw,"admin": gehashter_pw}

# ---------- SPLASH & LOGIN BLOCK ----------

def get_resource_path(dateiname):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, dateiname)
    return os.path.join(os.path.abspath("."), dateiname)


def show_splash_and_login():
    splash = ThemedTk(theme="winxpblue")
    splash.title("Ladeprogramm")
    splash.overrideredirect(True)
    screen_width = 950
    screen_height = 750
    center_x = (splash.winfo_screenwidth() // 2) - (screen_width // 2)
    center_y = (splash.winfo_screenheight() // 2) - (screen_height // 2)
    splash.geometry(f"{screen_width}x{screen_height}+{center_x}+{center_y}")
    style = ttk.Style()
    style.configure("Splash.TFrame", background="white")
    splash_frame = ttk.Frame(splash, style="Splash.TFrame")
    splash_frame.place(relwidth=1, relheight=1)
    try:
        bildpfad = get_resource_path("Badmeyer.png")
        if not os.path.isfile(bildpfad):
            raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")
        bg_image = tk.PhotoImage(file=bildpfad)
        background_label = tk.Label(splash_frame, image=bg_image)
        background_label.image = bg_image
        background_label.place(relx=0.5, rely=0.3, anchor="center")
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        label = ttk.Label(splash_frame, text="[Bild fehlt]", style="Splash.TFrame", foreground="white")
        label.place(relx=0.5, rely=0.8, anchor="center")
    ttk.Label(splash_frame, text="Wird geladen...").place(relx=0.5, rely=0.85, anchor="center")
    progress = ttk.Progressbar(splash_frame, orient="horizontal", length=300, mode="determinate")
    progress.place(relx=0.5, rely=0.9, anchor="center")

    def update_bar(value=0):
        progress["value"] = value
        if value < 100:
            splash.after(80, update_bar, value + 7)
        else:
            splash.after(500, login_screen)


        #Login Bildschirm 
    def login_screen():
        splash.destroy()
        login = ThemedTk(theme="winxpblue")
        login.title("Login")
        win_width = 500
        win_height = 300
        center_x = (login.winfo_screenwidth() // 2) - (win_width // 2)
        center_y = (login.winfo_screenheight() // 2) - (win_height // 2)
        login.geometry(f"{win_width}x{win_height}+{center_x}+{center_y}")
        style = ttk.Style()
        style.configure("Login.TFrame", background="white")
        login_frame = ttk.Frame(login, style="Login.TFrame")
        login_frame.place(relwidth=1, relheight=1)
        ttk.Label(login_frame, text="Benutzername").place(relx=0.5, rely=0.2, anchor="center")
        user_entry = ttk.Entry(login_frame)
        user_entry.place(relx=0.5, rely=0.3, anchor="center")
        ttk.Label(login_frame, text="Passwort").place(relx=0.5, rely=0.4, anchor="center")
        pass_entry = ttk.Entry(login_frame, show="*")
        pass_entry.place(relx=0.5, rely=0.5, anchor="center")
        def einloggen():
            username = user_entry.get().strip().lower()
            password = pass_entry.get().strip()

            if username and password:
                daten = do_login(user=username)
                if daten:
                    db_hash = daten[1]
                    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
                    if hashed_pw == db_hash:
                        login.destroy()
                        start_main_gui()

                else:
                    tk.messagebox.showerror("Login fehlgeschlagen", "Benutzername oder Passwort falsch!")
            else:
                tk.messagebox.showerror("Fehler", "Bitte Benutzername und Passwort eingeben.")
        ttk.Button(login_frame, text="Login", command=einloggen).place(relx=0.5, rely=0.7, anchor="center")
        login.mainloop()
    update_bar()
    splash.mainloop()

def start_main_gui():
    

    #Variablen
    global inputs
    inputs = {}

    #Fenster erstellen
    global root
    root = ThemedTk(theme="winxpblue")
    root.title ("Badmeyer")
    win_width = 1050
    win_height = 600
    center_x = (root.winfo_screenwidth() // 2) - (win_width // 2)
    center_y = (root.winfo_screenheight() // 2) - (win_height // 2)
    root.geometry(f"{win_width}x{win_height}+{center_x}+{center_y}")

    global main_frame, einzel_frame, gesamt_frame, logo_bild
    main_frame = ttk.Frame(root)
    main_frame.place(x=0, y=0, relwidth=1, relheight=1)

    start_label = ttk.Label(main_frame, text= " Willkommen im Badmeyer Verwaltungstool für Bestellungen!", font=("Arial", 14))
    start_label.place(relx=0.5, rely=0.2, anchor="center")

    try:
        bildpfad = get_resource_path("badmeyer_small.png")
        if not os.path.isfile(bildpfad):
            raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")
        start_bild = tk.PhotoImage(file=bildpfad)
        bild_label = ttk.Label(main_frame, image=start_bild)
        bild_label.image = start_bild  # Referenz behalten!
        bild_label.place(relx = 0.5, rely = 0.5, anchor="center")
    except Exception as fehler:
        print("Fehler beim Laden des Bildes:", fehler)
        bild_label = ttk.Label(main_frame, text="[Kein Bild verfügbar]")
        bild_label.place(relx = 0.5, rely = 0.5, anchor="center")

    start_label2 = ttk.Label(main_frame, text="Wählen Sie oben eine Ansicht aus", font=("Arial", 14))
    start_label2.place(relx=0.5, rely=0.8, anchor="center")



    einzel_frame = ttk.Frame(main_frame)
    gesamt_frame = ttk.Frame(main_frame)


    #bild global laden
    try:
        bildpfad = get_resource_path("badmeyer_small.png")
        if not os.path.isfile(bildpfad):
            raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")
        logo_bild = tk.PhotoImage(file=bildpfad)
    except Exception as fehler:
        print("Fehler beim Laden des Bildes:", fehler)
        logo_bild = None  

    #Frame Auswahl

    def zeige_frame(frame):
        
        for unterframe in main_frame.winfo_children():
            unterframe.place_forget()
        frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    #Tabelle leeren
    def tabelleleeren(tree):
        for item in tree.get_children():
            tree.delete(item)

    #Logout
    def logout():
        bestätigen = messagebox.askyesno("Abmelden", "Möchten Sie sich wirklich abmelden?")
        if bestätigen:
            root.destroy()
    

    #Auswahl Einzelsuche
    def einzelsuche():
        
        daten = []
            #Eingabefelder
        labels = ["ID:", "Vorname:", "Nachname:", "Produkte:"]
        inputs.clear()

            #Geht alle Feldnamen durch
        for i, label in enumerate(labels):
                #Zeigt den Text (ID, Name, etc.) links im Fenster an
                ttk.Label(einzel_frame, text=label).place(x=20, y=30 + i * 40)  #Position: 20 Pixel von links, und 40 Pixel nach unten versetzt
                eingabe = ttk.Entry(einzel_frame)  #Erstellt ein Textfeld
                eingabe.place(x=120, y=30 + i * 40, width=180)  #Position des Textfelds rechts neben dem Label
                inputs[label.strip(":")] = eingabe  #Speichert das Textfeld ohne Doppelpunkt

        #Monat-Auswahl als Dropdown
        ttk.Label(einzel_frame, text="ab Monat:").place(x=20, y=30 + len(labels) * 40)
        monat_combo = ttk.Combobox(einzel_frame, values=[
            "Januar", "Februar", "März", "April", "Mai", "Juni",
            "Juli", "August", "September", "Oktober", "November", "Dezember"
        ])
        monat_combo.place(x=120, y=30 + len(labels) * 40, width=180)
        inputs["Monat"] = monat_combo

            #Jahr-Auswahl als Dropdown
        ttk.Label(einzel_frame, text="ab Jahr:").place(x=20, y=30 + (len(labels) + 1) * 40)
        jahr_combo = ttk.Combobox(einzel_frame, values=["2024", "2025"])
        jahr_combo.place(x=120, y=30 + (len(labels) + 1) * 40, width=180)
        inputs["Jahr"] = jahr_combo

        #Spaltenüberschriften der Tabelle
        columns = ("ID", "Vorname", "Nachname", "Produkte", "Menge", "Monat", "Jahr")

        #Such-Button
        def suchen():
            id = inputs.get("ID").get().strip()
            vorname = inputs.get("Vorname").get().strip()
            nachname = inputs.get("Nachname").get().strip()
            produkt = inputs.get("Produkte").get().strip()
            monat_name = inputs.get("Monat").get().strip()
            jahr = inputs.get("Jahr").get().strip()


            #Prüft, ob der Monat gültig ist
            gültige_monate = [
                "Januar", "Februar", "März", "April", "Mai", "Juni",
                "Juli", "August", "September", "Oktober", "November", "Dezember"
            ]

            #Monate in zahl umwandeln
            monat = gültige_monate.index(monat_name) + 1 if monat_name in gültige_monate else None

            #überprüfung jahr
            jahr = int(jahr) if jahr.isdigit() else None


            daten = sql_einzelansicht(
                 id = id, 
                 vorname = vorname, 
                 nachname = nachname, 
                 produkt = produkt, 
                 menge = "", 
                 monat = monat, 
                 jahr = jahr
                 )

            
            #Tabelle leeren
            tabelleleeren(tabelle)


            # Neue Daten einfügen
            for datensatz in daten:
                tabelle.insert("", tk.END, values=datensatz)

            
        
        #Such-Button, der die Funktion "suchen" aufruft
        such_btn = ttk.Button(einzel_frame, text="Suchen", command=suchen)
        such_btn.place(x=120, y=25 + (len(labels) + 2) * 40, width=180)

        #leeren button
        btn_clear_einzel = ttk.Button(einzel_frame, text="Leeren", command=lambda: tabelleleeren(tabelle))
        btn_clear_einzel.place(x=120, y=55 + (len(labels)+2) * 40, width=180)


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


        #Badmeyer-Logo unten links
        try:
            bildpfad = get_resource_path("badmeyer_small.png")  #Pfad zur Bilddatei

            #Prüft, ob die Bilddatei existiert
            if not os.path.isfile(bildpfad):
                raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")

            #Bild laden
            if logo_bild:
                logo_label = tk.Label(einzel_frame, image=logo_bild)
                logo_label.image = logo_bild
                logo_label.place(x=60, y=370)  # Position des Bildes unten links

        #Falls beim Laden etwas schiefläuft, Ausgabe im Terminal
        except Exception as fehler:
            print("Fehler beim Laden des Bildes:", fehler)
            print("Aktueller Pfad:", os.getcwd())
            print("Dateien im Ordner:", os.listdir())

        

    def gesamtansicht():
        
        #Eingabefelder

        labels = ["ID-Kunde:", "Produkt:"]
        gesamt_inputs = {}

        for i, label in enumerate(labels):
            ttk.Label(gesamt_frame, text=label).place(x=20,y=30 + i *40)
            eingabe = ttk.Entry(gesamt_frame)
            eingabe.place(x=120, y=30 + i *40, width=180)
            gesamt_inputs[label.strip(":")] = eingabe

        #Monate(Combobox)

        label_monat = ttk.Label(gesamt_frame, text="Monat:")
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
        spalten = ("ID", "Vorname", "Nachname", "Produkt", "Menge", "Umsatz")

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

        spaltenbreiten = [40, 100, 100, 150, 80, 60]

        for i, spalte in enumerate(spalten):
            gesamt_tabelle.heading(spalte, text= spalte, anchor="center")
            gesamt_tabelle.column(spalte, width=spaltenbreiten[i], anchor="center")

        #suche für gesamtansicht

        def gesamt_suche():

            kunden_id = gesamt_inputs.get("ID-Kunde").get().strip()
            produkt = gesamt_inputs.get("Produkt").get().strip()
            monat_name = gesamt_inputs.get("Monat").get().strip()
            jahr_text = gesamt_inputs.get("Jahr").get().strip()


            gültige_monate = [
                "Januar", "Februar", "März", "April", "Mai", "Juni",
                "Juli", "August", "September", "Oktober", "November", "Dezember"
            ]

            monat = gültige_monate.index(monat_name) +1 if monat_name in gültige_monate else None

            #Jahr

            jahr = int(jahr_text) if jahr_text.isdigit() else None

            #nur kundenID zulässig

            if kunden_id and not kunden_id.isdigit():
                messagebox.showerror("Fehlker", "Kunden-ID muss eine Zahl sein")
                return
            
            #abfrage

            daten = sql_gesamtsuche(kunden_id, produkt, monat, jahr)

            #TV leeren
            for zeile in gesamt_tabelle.get_children():
                gesamt_tabelle.delete(zeile)

            #ergebnis

            for datensatz in daten:
                gesamt_tabelle.insert("", tk.END, values = datensatz)


        #suche button

        btn_suche = ttk.Button(gesamt_frame, text="Suchen", command= gesamt_suche)
        btn_suche.place(x=120, y=30 + (len(labels) + 2) *40, width=180)

        #leeren button
        btn_clear_einzel = ttk.Button(gesamt_frame, text="Leeren", command=lambda: tabelleleeren(gesamt_tabelle))
        btn_clear_einzel.place(x=120, y=55 + (len(labels)+2) * 40, width=180)

        # Bild unten links
        try:
            bildpfad = get_resource_path("badmeyer_small.png")
            if not os.path.isfile(bildpfad):
                raise FileNotFoundError(f"Datei nicht gefunden: {bildpfad}")
            if logo_bild:
                logo_label = tk.Label(gesamt_frame, image=logo_bild)
                logo_label.image = logo_bild
                logo_label.place(x=60, y=370)

        except Exception as fehler:
            print("Fehler beim Laden des Bildes (Gesamtsuche):", fehler)


    #Menu Erstellen
    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    my_menu.add_command(label="Einzelansicht", command= lambda: zeige_frame(einzel_frame))
    my_menu.add_command(label="Gesamtsuche", command= lambda: [gesamtansicht(), zeige_frame(gesamt_frame)])
    my_menu.add_command(label="Logout", command=logout)

    # #Anwendung wird gestartet
    einzelsuche()
    root.mainloop()