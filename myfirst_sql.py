import sqlite3
conn = sqlite3.connect('lihuan.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE lihuan(
id TEXT PRIMARY KEY ,
desc TEXT,
water FLOAT,
kcal FLOAT,
protein FLOAT,
fat FLOAT,
ash FLOAT,
carbs FLOAT,
fiber FLOAT,
sugar FLOAT
)''')
query = 'INSERT INTO lihuan VALUES (?,?,?,?,?,?,?,?,?,?)'
vals = [1,"i m a food",10,20,30,40,50,60,70,80]
curs.execute(query,vals)
conn.commit()
conn.close()