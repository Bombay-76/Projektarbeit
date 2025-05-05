import mariadb, sys


class Datenbank():
    def __init__(self):
        nummer = 0
        


try:#connect
    conn = mariadb.connect(
        user = "LNRD",
        password = "SWEDswed11",
        host = "localhost",
        port = 3306,
        database = "schlumpfshop3")
 
except mariadb.Error as e:
    print(f"Error connecting to MariaDB PLatform: {e}")
    sys.exit(1)
#get cursor
cur = conn.cursor()
#"SELECT artikel.Artikelname, artikel.Preis_Netto, artikel.Lagerbestand, lieferant.Lieferantenname FROM artikel INNER JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant;"
cur.execute(
    "SELECT * FROM anrede WHERE anrede = 'divers';")