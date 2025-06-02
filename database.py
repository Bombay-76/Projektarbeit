import os
import mariadb
import sys
import hashlib
from dotenv import load_dotenv
import mysql.connector
from GUI import *

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

    def register(self, mitarbeiter_nr, vorname, nachname, adresse, passwort):#FunktionZurÜbergabeDerEingegebenenValues
        try:
            hashed_pw = hashlib.sha256(passwort.encode()).hexdigest()#HashedDasEingegebenePasswort
            self.cur.execute(
                "INSERT INTO mitarbeiter (mitarbeiter_nr, vorname, nachname, adresse, passwort) VALUES (?, ?, ?, ?, ?)",
                (mitarbeiter_nr, vorname, nachname, adresse, hashed_pw)
            )
            self.conn.commit()
            print("Mitarbeiter registriert!")
        except mariadb.Error:
            print("Da hat etwas nicht geklappt!")
    
    def login(self, mitarbeiter_nr, passwort):
        try:
            hashed_pw = hashlib.sha256(passwort.encode()).hexdigest()
            self.cur.execute(
                "SELECT * FROM mitarbeiter WHERE mitarbeiter_nr = ? AND passwort = ?",#FürhtSQLCodeAus
                (mitarbeiter_nr, hashed_pw)
            )
            return self.cur.fetchone()
        except mariadb.Error:
            print("Da hat etwas nicht geklappt!")
    
    def insight(self):
        try:
            self.cur.execute("SELECT * FROM Zeiterfassung")
            daten = self.cur.fetchall()
            return daten
        except mariadb.Error:
            print("Da hat etwas nicht geklappt!")

    def add(self, projekt_id, projektname, kunden_nr):
        try:
            sql = "INSERT INTO Projekt (projekt_id, projektname, kunden_nr) VALUES (%s, %s, %s)"
            self.cur.execute(sql, (projekt_id, projektname, kunden_nr))
            self.conn.commit()
            print("Projekt erfolgreich hinzugefügt.")
        except:
            print(f"Da hat etwas nicht geklappt")

    def arbeitszeit(self, projekt_id, stunden):
        try:
            sql = "INSERT INTO Zeiterfassung (projekt_id, stunden) VALUES (%s, %s)"
            self.cur.execute(sql, (projekt_id, stunden))
            self.conn.commit()
            print("Arbeitszeit erfasst.")
        except:
            print(f"Da hat etwas nicht geklappt!")

    def delete(self):
        pass
    
    
    def close(self):#FunktionZumSchließenDerDatenbankConnection
        self.conn.close()
