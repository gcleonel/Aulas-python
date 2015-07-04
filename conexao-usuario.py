import sqlite3
db = sqlite3.connect("senac.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE usuario(id integer primary key autoincrement,
nome varchar(100) not null,
verbo varchar(100) not null,
qnt int)""")
db.commit()
