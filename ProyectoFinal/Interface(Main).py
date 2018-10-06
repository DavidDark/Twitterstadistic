#Esta es la clase Interface para el display de los datos obtenidos
#FRONTEN
import webbrowser
import os.path

if not os.path.isfile("holamundo.html"):
    f = open('holamundo.html','w')
    res = 12/3
    mensaje = """<html>
    <head></head>
    <body>
    <p>Hola Mundo!</p>
    <p>{}</p>
    </body>
    </html>""".format(res)

    f.write(mensaje)
    f.close()

    webbrowser.open_new_tab('holamundo.html')
else:
    webbrowser.open_new_tab('holamundo.html')

#Por ahora esta es una prueba de que funciona la clase main y se puede crear todo
#el mugrero de la aplicacion
