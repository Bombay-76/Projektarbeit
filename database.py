import tkinter as tk
import mariadb
import os
import sys
from dotenv import load_dotenv

class Datenbank:
    def __init__(self):
        load_dotenv()
        try:
            # Verbindung aufbauen
            self.conn = mariadb.connect(
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                host=os.getenv("HOST"),
                port=int(os.getenv("PORT")),
                database=os.getenv("DATABASE")
            )
            self.cur = self.conn.cursor()
            print("Verbindung erfolgreich hergestellt.")
        except mariadb.Error as e:
            print(f"Fehler beim Verbinden zu MariaDB: {e}")
            sys.exit(1)

    def register(self):
        try:
            self.cur.execute(
            "INSERT INTO mitarbeiter (mitarbeiter_id, adresse, geburtsdatum, passwort) VALUES (?, ?, ?, ?)"
            )
            results = self.cur.fetchall()
            print("Ergebnisse:")
            for row in results:
                print(row)
        except mariadb.Error as e:
            print(f"Fehler beim Ausführen des SQL-Befehls: {e}")

if __name__ == "__main__":
    app = Datenbank()
