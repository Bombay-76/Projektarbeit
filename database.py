import os
import mariadb
import sys
import hashlib
from dotenv import load_dotenv
import mysql.connector

class Datenbank:
    def __init__(self):
        if getattr(sys, 'frozen', False):
            basedir = sys._MEIPASS
        else:
            basedir = os.path.dirname(os.path.abspath(__file__))

        dotenv_path = os.path.join(basedir, ".env")
        load_dotenv(dotenv_path)

        host = os.getenv("HOST")
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        database = os.getenv("DATABASE")
        port_str = os.getenv("PORT")

        if port_str is None:
            raise ValueError("Die Umgebungsvariable PORT ist nicht gesetzt!")
        try:
            port = int(port_str)
        except ValueError:
            raise ValueError(f"PORT ({port_str}) ist keine gültige Zahl!")

        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            self.cur = self.conn.cursor()
            print("Verbindung hergestellt!")
        except mysql.connector.Error as e:
            print(f"Fehler beim Verbinden zur Datenbank: {e}")

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

    def add_1(self, projektname, kunden_nr):

        try:
            sql = "INSERT INTO Projekt (projektname, kunden_nr) VALUES (%s, %s)"
            self.cur.execute(sql, (projektname, kunden_nr))
            self.conn.commit()
            print("Projekt erfolgreich hinzugefügt.")
        except Exception:
            print(f"Fehler beim Hinzufügen des Projekts")

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
            self.cur.execute("SELECT * FROM Projekt")
            daten = self.cur.fetchall()
            print(f"{len(daten)} Projekte gefunden.")  # Hilfreich zum Debuggen
            return daten
        except Exception:
            print("Fehler bei Projektabfrage")
            return []

    def filter(self, kundennr):
        try:
            self.cur.execute("SELECT * FROM Projekt WHERE kunden_nr = %s", (kundennr,))
            return self.cur.fetchall()
        except Exception:
            print("Fehler bei der Abfrage")
            return []

        
    def close(self):#FunktionZumSchließenDerDatenbankConnection
        self.conn.close()
