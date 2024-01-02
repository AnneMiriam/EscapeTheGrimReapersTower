import sqlite3

CONN = sqlite3.connect('tower.db')
CURSOR = CONN.cursor()
