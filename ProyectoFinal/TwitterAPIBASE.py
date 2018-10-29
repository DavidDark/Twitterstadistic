import tweepy
import sqlite3
import os
from datetime import datetime
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
#ID en twitter, Nombre
#De donde es
#Verifidado o no
#Cuantos seguidores Tiene
#Cuantos tweets y retwitts ha hecho
#Cuantos personas sigue
#Tweets de los ultimos 15 días
#Lenguaje de su interface
#profile_image_url foto
#withheld_scope usado o no por un usuario


#Creacion de la tabla
def insert_db(handle,followers,description,tweets):
    conn = sqlite3.connect("social_data.db")
    cur = conn.cursor()
    cur.execute(''' INSERT INTO tabla VALUES (?,?,?,?,?)''', (datetime.now(), handle, followers, description, tweets))
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
cur.execute('''CREATE TABLE IF NOT EXISTS tabla
    (FetchDate Date, Handle Text, Followers Integer, Description Text, Tweets Text)
    ''')
conn.commit()
conn.close()
#Acciones Realizadas por la API para obtener los datos
for handle in handles_list:
    print ('Fetching %' + handle)
    try:
        user = api.get_user(screen_name=handle)
        #Ejemplos de lo que podemos obtener:
        #print ("Name:", user.name)
        #print ("Name:", user.screen_name)
        #print ("Number of tweets: " + str(user.statuses_count))
        #print ("followers_count: " + str(user.followers_count))
        #print ("Account location: ", user.location)
        #print ("Account created at: ", user.created_at)
        #print ("Account geo enabled: ", user.geo_enabled)
        tweets=str(user.statuses_count)
        followers = user.followers_count
        description = user.description


        #for friend in user.friends():
            #print (friend.screen_name)
        insert_db(handle,followers,description,tweets)
        #Se comprueba si el usuario existe
    except tweepy.error.TweepError:
        print ('-- ' + handle + ' not found')

#for tweet in public_tweets:
#    print (tweet.text)
