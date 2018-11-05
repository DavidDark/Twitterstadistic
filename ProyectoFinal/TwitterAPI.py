import tweepy
from tweepy import OAuthHandler

def Autentificacion(self,usuario):
    #Datos para Autentificación
    consumer_key = 'j7bXwQAiFE0EIcCrptRIbANGP'
    consumer_secret = 'WX41oCT4SOK12vZEQYPqM1KHw2sukIknTjWaleX8BvVahi7ull'
    access_token = '832311984-34Nv5J7AViBapsD22x8KZQE5mMPzcSaA2pzVbDyt'
    access_token_secret = 'zeIKKumVBMwOxEBDhJg8Qh7bDtu6bjne7QWi1qsFgfJ9A'
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    #Autentificación
    api = tweepy.API(auth)
    handles_list = [usuario]
