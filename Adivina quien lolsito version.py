import sqlite3

conn=sqlite3.connect('Lolsito.db')
c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS Lolsito (
    Nombre TEXT PRIMARY KEY,
    Humano REAL NOT NULL,
    Yordle REAL NOT NULL,
    Otra raza REAL NOT NULL,
    Demacia REAL NOT NULL,
    Bandle REAL NOT NULL,
    Zaun REAL NOT NULL,
    Freljord REAL NOT NULL,
    VAcio REAL NOT NULL,
    Piltover REAL NOT NULL,
    Otra_region REAL NOT NULL,
    Peleador REAL NOT NULL,
    Tanque REAL NOT NULL,
    Caster REAL NOT NULL,
    Tirador REAL NOT NULL) """)

#c.execute("INSERT INTO Lolsito VALUES ('Ashe',1,0,0,0,0,0,1,0,0,0,0,0,0,1)")
#c.execute("INSERT INTO Lolsito VALUES ('Jynx',1,0,0,0,0,1,0,0,0,0,0,0,0,1)")
#c.execute("INSERT INTO Lolsito VALUES ('Zylas',1,0,0,1,0,0,0,0,0,0,1,0,0,0)")
#c.execute("INSERT INTO Lolsito VALUES ('Garen',1,0,0,1,0,0,0,0,0,0,1,0,0,0)")
#c.execute("INSERT INTO Lolsito VALUES ('Urgot',1,0,0,0,0,1,0,0,0,0,0,1,0,0)")
#c.execute("INSERT INTO Lolsito VALUES ('Singed',1,0,0,0,0,1,0,0,0,0,0,1,0,0)")
#c.execute("INSERT INTO Lolsito VALUES ('Lulu',0,1,0,0,1,0,0,0,0,0,0,0,1,0)")
#c.execute("INSERT INTO Lolsito VALUES ('Lux',1,0,0,1,0,0,0,0,0,0,0,0,1,0)")
#c.execute("INSERT INTO Lolsito VALUES ('Teemo',0,1,0,0,1,0,0,,0,0,0,0,1,0)")
#c.execute("INSERT INTO Lolsito VALUES ('VelKoz',0,0,1,0,0,0,0,1,0,0,0,0,1,0)")
#conn.commit()

c.execute("SELECT * FROM Lolsito")
Lolsito=c.fetchall()

database=[]

for row in Lolsito:        
    database.append({'nombre':row[0],'humano':bool(row[1]),'yordle':bool(row[2]),'otra raza':bool(row[3]),'demacia':bool(row[4]),'bandle':bool(row[5]),'zaun':bool(row[6]),'freljord':bool(row[7]),'vacio':bool(row[8]),'piltover':bool(row[9]),'otra region':bool(row[10]),'peleador':bool(row[11]),'tanque':bool(row[12]),'caster':bool(row[13]),'tirador':bool(row[14])},)

def take_chance(answer,property):
    if answer == "s":
        ans=True
    else:
        ans=False

    to_remove=[]
    for d in database:
        if d[property]!=ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

ans=input("tu personaje es humano(S/N)")
take_chance(ans,"humano")
if ans=='s':
    ans1=1
else:
    ans1=0

ans=input("tu personaje es un yordle(S/N)")
take_chance(ans,"yordle")
if ans=='s':
    ans2=1
else:
    ans2=0

ans=input("tu personaje pertenece a otra raza?(S/N)")
take_chance(ans,"otra raza")
if ans=='s':
    ans3=1
else:
    ans3=0

ans=input("tu personaje es demaciano?(S/N)")
take_chance(ans,"demacia")
if ans=='s':
    ans4=1
else:
    ans4=0

ans=input("tu personaje es de bandle?(S/N)")
take_chance(ans,"bandle")
if ans=='s':
    ans5=1
else:
    ans5=0

ans=input("tu personaje es de zaun?(S/N)")
take_chance(ans,"zaun")
if ans=='s':
    ans6=1
else:
    ans6=0

ans=input("tu personaje es del freljord?(S/N)")
take_chance(ans,"freljord")
if ans=='s':
    ans7=1
else:
    ans7=0

ans=input("tu personaje es del vacio?(S/N)")
take_chance(ans,"vacio")
if ans=='s':
    ans8=1
else:
    ans8=0

ans=input("tu personaje es residente de piltover?(S/N)")
take_chance(ans,"piltover")
if ans=='s':
    ans9=1
else:
    ans9=0

ans=input("tu personaje es de otra region?(S/N)")
take_chance(ans,"otra region")
if ans=='s':
    ans10=1
else:
    ans10=0

ans=input("tu personaje es considerado peleador?(S/N)")
take_chance(ans,"peleador")
if ans=='s':
    ans11=1
else:
    ans11=0

ans=input("tu personaje es un saco de madrazos, un tanque?(S/N)")
take_chance(ans,"tanque")
if ans=='s':
    ans12=1
else:
    ans12=0

ans=input("tu personaje utiliza magia para pelear(caster)?(S/N)")
take_chance(ans,"caster")
if ans=='s':
    ans13=1
else:
    ans13=0

ans=input("tu personaje es un tirador?(S/N)")
take_chance(ans,"tirador")
if ans=='s':
    ans14=1
else:
    ans14=0


if len(database)==1:
    print("tu personaje es "+database[0]["nombre"])
else:
    print("No sepo cual era")
    print('que personaje era el que pensabas?')
    ans15=input()
    c.execute("INSERT INTO Lolsito VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(ans15,ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans9,ans9,ans10,ans11,ans12,ans13,ans14))
    conn.commit()

conn.close()
