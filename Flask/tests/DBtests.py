from models.orm import *
from database.db_drawingconstellation import DbDrawingConstellation
from database.db_planet import DBPlanet
from database.db_stars import DBStars
from database.db_user import DbUser
from database.db_constelations import DBConstellations
from common import cardinal_direction, stars_type

import unittest


def insertdata():
    cons = Constellations()
    cons.name = 'constellationsname'
    cons.declination = 'constellationdeclination'
    cons.symbolism = 'constellationsymbolism'
    cons.sky_side = 'sky_side'
    cons.area = 1.2

    draw = DrawingConstellation()
    draw.connected_Star = 1

    stars = Stars()
    stars.name = 'test'
    stars.rectascension = 'test'
    stars.declination = 'test'
    stars.radial_speed = 'test'
    stars.distance = 'test'
    stars.brightness = 'test'
    stars.star_type = 'test'
    stars.mass = 'test'
    stars.greek_symbol = 't'
    stars.constelation_id = 1
    stars.discaverer_id = 1
    stars.drawing_star = 1
    stars.constellation = cons
    stars.drawing = draw
    #stars.discaverer = user

    planet = Planet()
    planet.name = 'planet'
    planet.id_star = 1

    dbCons = DBConstellations(cons)
    dbCons.add_entity()

    drawings = DbDrawingConstellation(draw)
    drawings.add_entity()

    dbStars = DBStars(stars)
    dbStars.add_entity()

    dbPlan = DBPlanet(planet)
    dbPlan.add_entity()


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

    def testupdatenameuser(self):
        user = DbUser()
        self.assertTrue(user.update_name_surname_email(identyfikator, "adminT", "adminT", "admin@test.com"))

    def testupdateuserpassword(self):
        user = DbUser()
        self.assertTrue(user.update_password(identyfikator, "test1234"))

    def testgetdatauseranddelete(self):
        user = DbUser()
        self.assertTrue(user.delete_id(identyfikator))


class TestConstellation(unittest.TestCase):

    def testaddconstellation(self):
        constellation = Constellations()
        constellation.name = 'test'
        constellation.declination = '-10:20:30.0'
        constellation.symbolism = 'test'
        constellation.sky_side = cardinal_direction.CardinalDirection.North
        constellation.area = 123.4
        dbconstellation = DBConstellations(constellation)
        global identyfikator
        identyfikator = dbconstellation.add_entity()
        self.assertIsNotNone(identyfikator)

    def testconstellationdelete(self):
        dbconstellation = DBConstellations()
        self.assertTrue(dbconstellation.delete_id(identyfikator))


class TestStar(unittest.TestCase):

    def teststaradd(self):
        stars = Stars()
        stars.name = 'test'
        stars.rectascension = '10:20:30.1'
        stars.declination = '10:20:30.1'
        stars.radial_speed = '10'
        stars.distance = '100'
        stars.brightness = '1000'
        stars.star_type = stars_type.StarsType.dwarf
        stars.mass = '10000'
        stars.greek_symbol = 'Ω'
        stars.constelation_id = 21
        stars.discaverer_id = 62
        dbstar = DBStars(stars)
        self.assertIsNotNone(dbstar.add_entity())

class TestPlanet(unittest.TestCase):
    planet = Planet()
    planet.name = 'test'

