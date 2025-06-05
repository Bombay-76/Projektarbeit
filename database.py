#database.py datei 1
import os
import mariadb
import sys
import hashlib
from dotenv import load_dotenv
import mysql.connector

class Datenbank:
    def __init__(self):
        load_dotenv()#schütztdenzugangZurDatenbank
        try:
            #DatenbankConnection
            self.conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            port=int(os.getenv("PORT"))
        )
            self.cur = self.conn.cursor()
            print("Verbindung hergestellt!")
        except mariadb.Error:
            print("Da hat etwas nicht geklappt!")

    def register(self, mitarbeiter_nr, vorname, nachname, adresse, passwort):
        try:
            hashed_pw = hashlib.sha256(passwort.encode()).hexdigest()
            sql = "INSERT INTO mitarbeiter (mitarbeiter_nr, vorname, nachname, adresse, passwort) VALUES (%s, %s, %s, %s, %s)"
            self.cur.execute(sql, (mitarbeiter_nr, vorname, nachname, adresse, hashed_pw))
            self.conn.commit()
            print("Erfolgreich registriert!")
        except Exception:
            print("Fehler bei Registrierung")

    def login(self, mitarbeiter_nr, passwort):
        try:
            hashed_pw = hashlib.sha256(passwort.encode()).hexdigest()
            self.cur.execute(
                "SELECT * FROM mitarbeiter WHERE mitarbeiter_nr = %s AND passwort = %s",
                (mitarbeiter_nr, hashed_pw)
            )
            return self.cur.fetchone()
        except Exception:
            print("Login-Fehler")

    def add(self, projekt_id, projektname, kunden_nr):
        try:
            sql = "INSERT INTO Projekt (projekt_id, projektname, kunden_nr) VALUES (%s, %s, %s)"
            self.cur.execute(sql, (projekt_id, projektname, kunden_nr))
            self.conn.commit()
            print("Projekt erfolgreich hinzugefügt.")
        except Exception as e:
            print(f"Fehler beim Hinzufügen des Projekts: {e}")


    def arbeitszeit(self, projekt_id, stunden):
        try:
            sql = "INSERT INTO Zeiterfassung (projekt_id, stunden) VALUES (%s, %s)"
            self.cur.execute(sql, (projekt_id, stunden))
            self.conn.commit()
            print("Arbeitszeit erfasst.")
        except:
            print("Da hat etwas nicht geklappt!")

    def insight(self):
        try:
            self.cur.execute("SELECT * FROM projekt")
            return self.cur.fetchall()
        except:
            print("Da hat etwas nicht geklappt")
            return []

    def filter(self, kundennr):
        try:
            self.cur.execute("SELECT * FROM projekt WHERE kunden_nr = %s", (kundennr,))
            return self.cur.fetchall()
        except Exception:
            print(f"Fehler beim Filtern")
            return []
        
    def close(self):#FunktionZumSchließenDerDatenbankConnection
        self.conn.close()
