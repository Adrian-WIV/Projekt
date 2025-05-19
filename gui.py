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