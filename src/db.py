__author__ = 'Diogo'

import sqlite3

db = sqlite3.connect('test')

cursor = db.cursor()
cursor.execute('DROP TABLE IPC')
cursor.execute(('CREATE TABLE IPC(ano INTEGER PRIMARY KEY, ipc REAL, va REAL, remmax REAL, remmin REAL,\n'
                '    PIBpercap REAL, rnbpca REAL, rdbpca REAL, rpca REAL)'))

cursor.execute('INSERT INTO IPC VALUES(1977, 100, NULL, 22.4, 108.7, 421.6, 416.3, 443.4, 258.2)')

db.commit()

