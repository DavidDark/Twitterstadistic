import unittest
from unittest.mock import Mock
from twitter_ap import AppTwitter
from Tweet import *
from baseladvd import basedb

class Test(unittest.TestCase):

    def setUp(self):

        self.tw = AppTwitter()
        self.usuariomock = Mock(user_id = "547391733", handle = "SkaterZombie8", lugar = "Saltillo Coahuila",\
        verificado = "Usuario no verificado.",  followers = 22, numtweets = 71, friends = 72,\
        description = "Futuro Ing. En sistemas", lenguaje = "es",\
         profile = "http://pbs.twimg.com/profile_images/953711785185390592/iclwWUQn_normal.jpg",\
         Ranking = None,Categoria = None,Victorias = 0,Derrotas = 0)
        self.usuario = Tweeti(self.usuariomock.user_id,self.usuariomock.handle,self.usuariomock.lugar,\
        self.usuariomock.verificado,self.usuariomock.followers,self.usuariomock.numtweets,\
        self.usuariomock.friends,self.usuariomock.description,self.usuariomock.lenguaje,\
        self.usuariomock.profile,self.usuariomock.Ranking,self.usuariomock.Categoria,self.usuariomock.Victorias,\
        self.usuariomock.Derrotas)

        self.sql = basedb()
        self.sql.insert_db(self.usuario)

        self.usuario1 = Tweeti('15228314','Moco','Demacia','chi',2,70000,4,'','es','url',None,None,0,0)

    def tearDown(self):
        print("Fin de la prueba")

    #Hace las pruebas de guardar
    def test_Usuario(self):

        print("test_Usuario")
        self.assertEqual(self.usuario1.user_id, '15228314')
        self.assertEqual(self.usuario1.handle, 'Moco')
        self.assertEqual(self.usuario1.lugar, 'Demacia' )
        self.assertEqual(self.usuario1.verificado, "chi" )
        self.assertEqual(self.usuario1.followers, 2 )
        self.assertEqual(self.usuario1.numtweets, 7000 )
        self.assertEqual(self.usuario1.friends, 4 )
        self.assertEqual(self.usuario1.description, '')
        self.assertEqual(self.usuario1.lenguaje, 'es')
        self.assertEqual(self.usuario1.profile, 'url')
        self.assertEqual(self.usuario1.Ranking, None)
        self.assertEqual(self.usuario1.Categoria, None)
        self.assertEqual(self.usuario1.Victorias, 0)
        self.assertEqual(self.usuario1.Derrotas, 0)

        #Tipo de dato
        self.assertNotEqual(self.usuario1.followers, '2' )
        self.assertNotEqual(self.usuario1.numtweets, '7000' )
        self.assertNotEqual(self.usuario1.friends, '4')
        self.assertNotEqual(self.usuario1.Victorias, '0')
        self.assertNotEqual(self.usuario1.Derrotas, '0')


    def testinsert(self):
        print("testinsert")
        self.assertTrue(self.sql.insert_db(self.tw.getUsuario("SkaterZombie8")))

    def testupdate(self):
        print("test_update")
        self.assertTrue(self.sql.updateUsuario(self.usuario.handle,self.usuario.Ranking,\
        self.usuario.Categoria,self.usuario.Victorias,self.usuario.Derrotas))

    def testborrar(self):
        print("test_borrar")
        self.assertTrue(self.sql.deleteUsuario(self.usuario.handle))

    def test_getUsuario(self):
        print("test_getUsuario")
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").user_id, self.usuario.user_id)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").handle, self.usuario.handle)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").lugar, self.usuario.lugar)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").verificado, self.usuario.verificado)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").followers, self.usuario.followers)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").numtweets, self.usuario.numtweets)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").friends, self.usuario.friends)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").description, self.usuario.description)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").lenguaje, self.usuario.lenguaje)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").profile, self.usuario.profile)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").Ranking, self.usuario.Ranking)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").Categoria, self.usuario.Categoria)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").Victorias, self.usuario.Victorias)
        self.assertEqual(self.tw.getUsuario("SkaterZombie8").Derrotas, self.usuario.Derrotas)

if __name__ == '__main__':
    unittest.main()
