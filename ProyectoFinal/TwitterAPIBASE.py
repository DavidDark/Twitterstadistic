import tweepy
import sqlite3
import os
from tweepy import OAuthHandler
#Datos para Autentificación
consumer_key = 'j7bXwQAiFE0EIcCrptRIbANGP'
consumer_secret = 'WX41oCT4SOK12vZEQYPqM1KHw2sukIknTjWaleX8BvVahi7ull'
access_token = '832311984-34Nv5J7AViBapsD22x8KZQE5mMPzcSaA2pzVbDyt'
access_token_secret = 'zeIKKumVBMwOxEBDhJg8Qh7bDtu6bjne7QWi1qsFgfJ9A'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Autentificación
api = tweepy.API(auth)
handles_list = ['DavidDarkXD','Armando31647954']

#Creacion de la tabla
def insert_db(user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile):
    conn = sqlite3.connect("social_data.db")
    cur = conn.cursor()
    cur.execute(''' INSERT INTO tabla VALUES (?,?,?,?,?,?,?,?,?,?)''', (user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile))
    conn.commit()
    conn.close()
#Si no existe la base de datos, entonces se Crea
if not os.path.isfile("social_data.db"):
    conn = sqlite3.connect("social_data.db")
    conn.close()
else:
    pass

#Si la tabla no existe en la base, entonces la crea
conn = sqlite3.connect("social_data.db")
cur = conn.cursor()
cur.executescript('drop table if exists tabla;')
cur.execute('''CREATE TABLE IF NOT EXISTS tabla
    (ID Text, Nombre Text, Lugar Text, Verificado Text, Followers Integer, Tweets y Retweets Integer, Following Integer, Descipcion Text, Lenguaje Text, Foto Text)
    ''')
conn.commit()
conn.close()
#Acciones Realizadas por la API para obtener los datos
for handle in handles_list:
    print ('Fetching %' + handle)
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

        insert_db(user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile)
        #Se comprueba si el usuario existe
    except tweepy.error.TweepError:
        print ('-- ' + handle + ' not found')
