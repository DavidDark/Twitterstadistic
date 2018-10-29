

import os
from datatime import datatime


class BDS(AbstractObject):
#Creacion de la tabla
    def insert_db(handle,followers,description,ID):
        conn = sqlite3.connect("social_data.db")
        cur = conn.cursor()
        if not os.path.exist("social_data.db"):
            conn = sqlite3.connect("social_data.db")
        else:
            pass
        cur.execute('''CREATE TABLE IF NOT EXISTS tabla
        (ID Text FetchDate Date, Handle Text, Followers Integer, Description Text)
        ''')
        conn.commit()
        cur.execute(''' INSERT INTO tabla VALUES (?,?,?,?,?):''', (ID,datatime.now(), handle, followers, description))
        conn.commit()
        conn.close()
        return 'Datos Incertados ({}, {}, {})'.format(handle,followers,description)

    #Si no existe la base de datos, entonces se Crea

    #Si la tabla no existe en la base, entonces la crea
    #Acciones Realizadas por la API para obtener los datos
    def Get_datos(self,handle):
        for handle in handles_list:
            return ('Fetching %' + handle)
            try:
                user = api.get_user(handle)
                followers = user.followers_count
                description = user.description

                for friend in user.friends():
                    print (friend.screen_name)
                    insert_db(handle,followers,description)
                except:
                    print ('-- ' + handle + ' not found')
