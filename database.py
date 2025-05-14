import tkinter as tk
import mariadb
import os
import sys
import hashlib
from dotenv import load_dotenv

class Datenbank:
    def __init__(self):
        load_dotenv()
        try:
            #DatenbankConnection
            self.conn = mariadb.connect(
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                host=os.getenv("HOST"),
                port=int(os.getenv("PORT")),
                database=os.getenv("DATABASE")
            )
            self.cur = self.conn.cursor()
            print("Verbindung hergestellt!")
        except mariadb.Error:
            print("Da hat etwas nicht geklappt!")

    def register(self, mitarbeiter_nr, vorname, nachname, adresse, passwort):
        try:
            hashed_pw = hashlib.sha256(passwort.encode()).hexdigest()
            self.cur.execute(
                "INSERT INTO mitarbeiter (mitarbeiter_nr, vorname, nachname, adresse, passwort) VALUES (?, ?, ?, ?, ?)",
                (mitarbeiter_nr, vorname, nachname, adresse, hashed_pw)
            )
            self.conn.commit()
            print("Erfolgreich registriert!")
        except mariadb.Error:
            print("Da hat etwas nicht geklappt!")
    
    def login(self, mitarbeiter_nr, passwort):
        try:
            hashed_pw = hashlib.sha256(passwort.encode()).hexdigest()
            self.cur.execute(
                "SELECT * FROM mitarbeiter WHERE mitarbeiter_nr = ? AND passwort = ?",
                (mitarbeiter_nr, hashed_pw)
            )   
            return self.cur.fetchone()
        except mariadb.Error:
            print("Da hat etwas nicht geklappt:")
    
    def insight():