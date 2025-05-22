"""
    20250428
    Projektarbeit 2. Halbjahr
    Stundenrechner
    Bombay-76
    Leonard
"""

import GUI
import database
import styles

data_obj = database.Datenbank()

mitarbeiter_nr, hashed_pw = data_obj.login()
