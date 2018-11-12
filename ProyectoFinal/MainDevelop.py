#Este archivo sirve pare probar el sistema desde la terminal
#Lleva un switch case para testear que el CRUD se haga correctamente
#NO CONFUNDIR ESTE ARCHIVO CON EL TEST !!!
import Usuario

print("Bienvenido al Sistema, elija una opción: ")
option= int(input("Buscar Usuario: 1 \nCrear Usuario: 2 \nActualizar Usuario: 3 \nBorrar Usuario: 4 \n"))
cont = 0
while cont == 0:
    if option == 1:
        usr = input("Introduzca un Usuario:")
        res = Usuario.getUsuario(usr)
        print(res)
    elif option == 2:
        usuario = input("Introduzca un Usuario:")
        res = Usuario.setUsuario(usuario)
        print(res)
    elif option == 3:
        usuario = input("Introduzca el Usuario a actualizar:")
        res1= Usuario.getUsuario(usuario)
        if res1 == 'El usuario: {} ,no existe'.format(usuario):
            print("Usuario No Encontrado.")
        else:
            rank = input("Puesto en el Ranking:")
            categ = input("Categoria:")
            v = input("Número de Victorias:")
            d = input("Número de Derrotas:")
            res = Usuario.updateUsuario(usuario,rank,categ,v,d)
            print(res)
    elif option == 4:
        usuario = input("Introduzca el Usuario a eliminar:")
        res = Usuario.deleteUsuario(usuario)
        print(res)
    else:
        print("Introduzca una opción válida.\n")
    cont= 1
