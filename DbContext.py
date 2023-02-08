import mariadb as Sql
from datetime import timedelta
import re

Param_Conn = {"host": "192.168.0.37", "user": "Gomsil", "password": "Gomsil123"}

# Connessione al database OreProd #
def Connect():
    global Param_Conn
    Param_Conn["database"] = "OreProd"
    try:
        ConnOre = Sql.connect(**Param_Conn)
        return ConnOre
    except:
        return False

# Connessione Database GomsilDB
def ConnGomsil():
    global Param_Conn
    Param_Conn["database"] = "GomsilDB"
    try:
        ConnGomsil = Sql.connect(**Param_Conn)
        return ConnGomsil
    except:
        return False

# Tabella Completa Ordinata x Anno Descendente #
def GetAllData(Tabella): 
    Connection = Connect()
    Cursor = Connection.cursor()
    Cursor.execute(f"Select * From {Tabella} Order By Anno Desc")
    return Cursor.fetchall()

# Calcola Tempo Lavoro #
def CalcolaTempo(Tabella, Data):
    Conn = ConnGomsil()
    Cur = Conn.cursor()
    Cur.execute(f"Select Ora From {Tabella} Where Data Like \"{Data}\" Order By RowId Desc")
    ListaOre = Cur.fetchall()
    if not bool(Cur.rowcount): return 0.0
    Sep = re.search("[.:]", ListaOre[0][0]).group()
    Totale = 0
    Hms1 = ListaOre[0][0].split(Sep)
    for Ora in ListaOre:
        Ora1 = timedelta(hours=int(Hms1[0]), minutes=int(Hms1[1]), seconds=int(Hms1[2]))
        Hms2 = Ora[0].split(Sep)
        Ora2 = timedelta(hours=int(Hms2[0]), minutes=int(Hms2[1]), seconds=int(Hms2[2]))
        Hms1 = Hms2
        if Ora1.seconds < Ora2.seconds: continue
        if (Ora1.seconds - Ora2.seconds) < 1800: Totale += Ora1.seconds - Ora2.seconds
    return "{:.2f}".format(Totale / 3600)

def Registra(Tabella, Colonna, Anno, Dato):
    try:
        Conn = Connect()
        Cur = Conn.cursor()
        Cur.execute(f"Update {Tabella} Set {Colonna} = \"{Dato}\" Where Anno = \"{Anno}\"")
        Conn.commit()
    except:
        return False

    
