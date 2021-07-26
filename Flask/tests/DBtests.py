from models.orm import *
from database.db_drawingconstellation import DbDrawingConstellation
from database.db_planet import DBPlanet
from database.db_stars import DBStars
from database.db_user import DbUser
from database.db_constelations import DBConstellations

import unittest

def insertdata():
    cons = Constellations()
    cons.name = 'constellationsname'
    cons.declination = 'constellationdeclination'
    cons.symbolism = 'constellationsymbolism'
    cons.sky_side = 'sky_side'
    cons.area = 1.2

    user = User()
    user.name = 'admin'
    user.surname = 'admin'
    user.login = 'admin'
    user.password = 'admin'
    user.email = 'admin'

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
    stars.discaverer = user

    planet = Planet()
    planet.name = 'planet'
    planet.id_star = 1

    dbCons = DBConstellations(cons)
    dbCons.add_entity()

    users = DbUser(user)
    users.add_entity()

    drawings = DbDrawingConstellation(draw)
    drawings.add_entity()

    dbStars = DBStars(stars)
    dbStars.add_entity()

    dbPlan = DBPlanet(planet)
    dbPlan.add_entity()


class TestMetthods(unittest.TestCase):
    def testgetdatastar(self):
        dbstars = DBStars()
        self.assertIsNotNone(dbstars.get_all())

    def testlistofstar(self):
        drawing = DbDrawingConstellation()
        self.assertIsNotNone(drawing.returnlist(10))

    def testconstelationsget(self):
        constellation = DBConstellations()
        self.assertIsNotNone(constellation.get_all())

    def testgetdataplanet(self):
        planet = DBPlanet()
        self.assertIsNotNone(planet.get_all())

    def testgetdatauser(self):
        user = DbUser()
        self.assertIsNotNone(user.get_all())

    def testupdatenameuser(self):
        user = DbUser()
        self.assertTrue(user.update_name_surname_email(20, "adminT", "adminT", "admin@test.com"))

    def testupdateuserpassword(self):
        user = DbUser()
        self.assertTrue(user.update_password(20, "test1234"))

    def testdeleteuser(self):
        user = DbUser()
        self.assertTrue(user.delete_id(1))
