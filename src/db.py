__author__ = 'Diogo'

import sqlite3


class Database:
    db = ''
    data = ''
    cursor = ''

    def __init__(self, data):
        Database.db = sqlite3.connect('test')
        Database.data = data
        Database.cursor = Database.db.cursor()



    def create_db(self):
        Database.cursor.execute(
            ('CREATE TABLE IPC(ano INTEGER PRIMARY KEY, ipc REAL, va REAL, remmax REAL, remmin REAL,\n'
             '    PIBpercap REAL, rnbpca REAL, rdbpca REAL, rpca REAL)'))
        Database.db.commit()

    def insert_data(self, data):
        for row in data




