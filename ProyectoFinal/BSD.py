import os
import TwitterAPI

class BDS(AbstractObject):
#Creacion de la tabla
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

    #Acciones Realizadas por la API para obtener los datos
    def Get_datos(self,handle):
        for handle in handles_list:
            return ('Fetching %' + handle)
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
                print ('-- ' + handle + ' not found')
