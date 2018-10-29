import tweepy
from tweepy import OAuthHandler

def Autentificaci(self,usuario):
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)

#Autentificación
    api = tweepy.API(auth)
    handles_list = [usuario]
