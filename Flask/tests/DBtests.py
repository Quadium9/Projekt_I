from models.orm import *
from database.db_drawingconstellation import DbDrawingConstellation
from database.db_planet import DBPlanet
from database.db_stars import DBStars
from database.db_user import DbUser
from database.db_constelations import DBConstellations
from common import cardinal_direction, stars_type
from flask import request
import unittest


class TestUser(unittest.TestCase):

    def testadduser(self):
        user = User()
        user.name = 'admin'
        user.surname = 'admin'
        user.login = 'admin'
        user.password = 'adminadmin'
        user.email = 'admin@admin.admin'
        dbuser = DbUser(user)
        global identyfikator
        identyfikator = dbuser.add_entity()
        self.assertIsNotNone(identyfikator)

    def testgetdatauseranddelete(self):
        user = DbUser()
        self.assertTrue(user.delete_id(identyfikator))

    def testloginuser(self):
        user = DbUser()
        tmp = user.get_one_by_name("admin")
        self.assertIsNotNone(user.get_one_by_name("admin"))


class TestConstellation(unittest.TestCase):

    def testaddconstellation(self):
        constellation = Constellations()
        constellation.name = 'test2'
        constellation.declination = '-10:20:30.0'
        constellation.symbolism = 'test'
        constellation.sky_side = cardinal_direction.CardinalDirection.North.value
        constellation.area = 123.4
        dbconstellation = DBConstellations(constellation)
        global identyfikator
        identyfikator = dbconstellation.add_entity()
        self.assertIsNotNone(identyfikator)

    def testconstellationdelete(self):
        dbconstellation = DBConstellations()
        self.assertTrue(dbconstellation.delete_id(21))

    def testconstellationget(self):
        dbconstellation = DBConstellations()
        print(dbconstellation.get_all())
        self.assertIsNotNone(dbconstellation.get(23))


class TestStar(unittest.TestCase):

    def teststaradd(self):
        stars = Stars()
        stars.name = 'testowy'
        stars.rectascension = '10:22:30.1'
        stars.declination = '10:22:30.1'
        stars.radial_speed = '10'
        stars.distance = '100'
        stars.brightness = '1000'
        stars.star_type = stars_type.StarsType.browndwarf.value
        stars.mass = '100001'
        stars.greek_symbol = 'Ω'
        stars.constelation_id = 21
        stars.discaverer_id = 62
        dbstar = DBStars(stars)
        global identy
        identy = dbstar.add_entity()
        self.assertIsNotNone(identy)

    def teststarget(self):
        dbstar = DBStars()
        self.assertIsNotNone(dbstar.get(17))

    def testgetdatabyname(self):
        dbstar = DBStars()
        print(dbstar.get_one_by_name('test'))
        self.assertIsNotNone(dbstar.get_one_by_name('test'))

    def testdeletestar(self):
        dbstars = DBStars()
        self.assertTrue(dbstars.delete_id(11))


class TestPlanet(unittest.TestCase):

    def testaddplanet(self):
        planet = Planet()
        planet.name = 'test'
        planet.id_star = 12
        dbplanet = DBPlanet(planet)
        self.assertIsNotNone(dbplanet.add_entity())

    def testgetplanet(self):
        dbplanet = DBPlanet()
        self.assertIsNotNone(dbplanet.get(11))

    def testupdateplanet(self):
        planet = Planet()
        planet.name = 'Test'
        planet.id_star = 12
        dbplanet = DBPlanet(planet)
        self.assertIsNotNone(dbplanet.update_entity(11))

    def testdeleteplanet(self):
        dbplanet = DBPlanet()
        self.assertTrue(dbplanet.delete_id(11))


class TestDrawingConstellation(unittest.TestCase):

    def testadddrawingconstellation(self):
        drawingconstellation = DrawingConstellation()
        drawingconstellation.connected_Star = 12
        dbdrawingconstellation = DbDrawingConstellation(drawingconstellation)
        self.assertIsNotNone(dbdrawingconstellation.add_entity())

    def testupdatedrawingconstellation(self):
        drawingconstellation = DrawingConstellation()
        drawingconstellation.connected_Star = 13
        dbdrawingconstellation = DbDrawingConstellation(drawingconstellation)
        self.assertIsNotNone(dbdrawingconstellation.update_entity(21))
