import sqlite3
import TwitterAPI
import os
import tweepy
def getUsuario(usuario):
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

def setUsuario(handle):
    #usr = usuario
    #res = BSD.Get_datos(usr)
    #return res
    api = TwitterAPI.Autentificacion()
    try:
        user = api.get_user(screen_name=handle)
        user_id = user.id_str
        lugar = user.location

        if (user.verified == True):
            verificado = 'Si.'
        else:
            verificado = 'Usuario no verificado.'

        followers = user.followers_count
        numtweets= user.statuses_count
        friends = user.friends_count

        if (user.description == ''):
            description = 'No tiene.'
        else:
            description = user.description

        lenguaje = user.lang
        profile = user.profile_image_url
        Ranking= None
        Categoria= None
        Victorias= 0
        Derrotas= 0

        insert_db(user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile,Ranking,Categoria,Victorias,Derrotas)
        #Se comprueba si el usuario existe
    except tweepy.error.TweepError:
        return ('-- ' + handle + ' not found')
    return ('Fetching %' + handle)

def deleteUsuario(usuario):
    conn = sqlite3.connect("social_data.db")
    c = conn.cursor()
    usr = usuario
    c.execute("SELECT * FROM tabla WHERE Nombre = ?",(usr,))
    datos = c.fetchone()
    if datos:
        c.execute("DELETE FROM tabla WHERE Nombre = ?",(usr,))
        conn.commit()
        return('El usuario: {} ,fue eliminado.'.format(usr))
    else:
        return('El usuario: {} ,no existe'.format(usr))
    conn.close()

def updateUsuario(handle,Ranking,Categoria,Victorias,Derrotas):
    conn = sqlite3.connect("social_data.db")
    c = conn.cursor()
    usr = handle
    c.execute("SELECT * FROM tabla WHERE Nombre = ?",(usr,))
    datos = c.fetchone()
    if datos:
        c.execute("UPDATE tabla SET Ranking= ?,Categoria= ?,Victorias= ?,Derrotas= ? WHERE Nombre= ?",\
        (Ranking,Categoria,Victorias,Derrotas,usr,))
        conn.commit()
        return('El usuario: {} ,fue actualizado.'.format(usr))
    else:
        return('El usuario: {} ,no existe'.format(usr))

    conn.close()

def insert_db(user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile,Ranking=None,Categoria=None,Victorias=0,Derrotas=0):
    conn = sqlite3.connect("social_data.db")
    cur = conn.cursor()
    if not os.path.isfile("social_data.db"):
        conn = sqlite3.connect("social_data.db")
    else:
        pass
    cur.execute('''CREATE TABLE IF NOT EXISTS tabla
        (ID Text,Nombre Text,Lugar Text,Verificado Text,Followers Integer,Tweets y Retweets Integer,Following Integer,Descipcion Text,Lenguaje Text,Foto Text,Ranking Text,Categoria Text,Victorias Integer, Derrotas Integer)
        ''')
    conn.commit()
    cur.execute(''' INSERT INTO tabla VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile,Ranking,Categoria,Victorias,Derrotas))
    conn.commit()
    conn.close()
    return 'Datos Insertados ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile,Ranking,Categoria,Victorias,Derrotas)
