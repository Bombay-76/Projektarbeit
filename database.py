import os, mariadb, sys
from dotenv import load_dotenv, dotenv_values


class Datenbank():
    def __init__(self):
        nummer = 0

        load_dotenv()

        try:#connect
            conn = mariadb.connect(
                user = os.getenv("USER"),
                password = os.getenv("PASSWORD"),
                host = os.getenv("HOST"),
                port = os.getenv("PORT"),
                database = os.getenv("DATABASE")
            )

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB PLatform: {e}")
            sys.exit(1)
        #get cursor
        cur = conn.cursor()
        #"SELECT artikel.Artikelname, artikel.Preis_Netto, artikel.Lagerbestand, lieferant.Lieferantenname FROM artikel INNER JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant;"
        cur.execute(
            "SELECT * FROM anrede WHERE anrede = 'divers';"
            )