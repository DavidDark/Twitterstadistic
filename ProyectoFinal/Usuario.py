import sqlite3
import BSD

def getUsuario(self,usuario):
    # Connecting to the database file
    conn = sqlite3.connect("social_data.db")
    c = conn.cursor()
    usr = usuario
    #Check if a certain ID exists and print its column contents
    c.execute("SELECT * FROM tabla WHERE Nombre = ?",(usr,))
    datos = c.fetchone()
    if datos:
        return('ID: {} \nNombre: {} \nLugar: {} \nVerificado: {} \nFollowers: {} \nTweets y Retweets: {} \nFollowing: {} \nDescipcion: {} \nLenguaje: {} \nFoto: {} \nRanking: {} \nCategoria: {} \nVictorias: {} \nDerrotas: {}'.\
        format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11],datos[12],datos[13]))
    else:
        return('El usuario: {} ,no existe'.format(usr))

    # Closing the connection to the database file
    conn.close()

def setUsuario(self,usuario):
    usr = usuario
    res = BSD.Get_datos(usr)
    return res

def deleteUsuario(self,usuario):
    conn = sqlite3.connect("social_data.db")
    c = conn.cursor()
    usr = usuario
    c.execute("DELETE FROM tabla WHERE Nombre = ?",(usr,))
    return('El usuario: {} ,fue eliminado.'.format(usr))

    conn.commit()
    conn.close()

def updateUsuario(self,handle,Ranking=None,Categoria=None,Victorias=0,Derrotas=0):
    conn = sqlite3.connect("social_data.db")
    c = conn.cursor()
    usr = handle
    c.execute("SELECT * FROM tabla WHERE Nombre = ?",(usr,))
    datos = c.fetchone()
    if datos:
        c.execute("UPDATE tabla SET Ranking= ?,Categoria= ?,Victorias= ?,Derrotas= ? WHERE Nombre= ?",\
        (Ranking,Categoria,Victorias,Derrotas,usr,))
        return('El usuario: {} ,fue actualizado.'.format(usr))
    else:
        return('El usuario: {} ,no existe'.format(usr))

    conn.commit()
    conn.close()
