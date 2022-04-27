from PyQt5.QtWidgets import QMessageBox
import sqlite3
from sqlite3 import Error


def _createSatisfactory(db_file):
    """create blank Database"""
    connection = sqlite3.connect(db_file)

    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS factory
                ("name"	TEXT NOT NULL,"production" TEXT NOT NULL,"building" TEXT NOT NULL,"recipe" TEXT NOT NULL,
                "building_quantity" INTEGER NOT NULL,"eff_clockspeed" INTEGER DEFAULT 1,"delivery_to" TEXT,
                PRIMARY KEY("name"))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS "resources" 
    ("name"	TEXT NOT NULL, "resource" TEXT NOT NULL, "mk_version" INTEGER NOT NULL DEFAULT 1, "quality"	TEXT NOT NULL, 
    "quantity_buildings" INTEGER NOT NULL DEFAULT 1, PRIMARY KEY("name"))''')



def createConnection(db_file):
    """Create and open a database connection."""
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    _createSatisfactory(db_file)
    return True
