from models.orm import *
from database.db_drawingconstellation import DbDrawingConstellation
from database.db_stars import DBStars
from database.db_user import DbUser
from database.db_constelations import DBConstellations
from common import cardinal_direction, stars_type
from flask import request
import unittest


class TestUser(unittest.TestCase):

    def testadduser(self):
        user = User()
        user.name = 'user'
        user.surname = 'user'
        user.login = 'user'
        user.password = 'useruser'
        user.email = 'user@user.user'
        user.rules = 'user'
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

    def testconstellationget(self):
        dbconstellation = DBConstellations()
        print(dbconstellation.get(130))
        self.assertIsNotNone(dbconstellation.get(130))


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
        print(dbstar.get_all())
        rt = dbstar.get_all()
        self.assertIsNotNone(rt)

    def testgetdatabyname(self):
        dbstar = DBStars()
        print(dbstar.get_one_by_name('test'))
        self.assertIsNotNone(dbstar.get_one_by_name('test'))

    def testdeletestar(self):
        dbstars = DBStars()
        self.assertTrue(dbstars.delete_id(11))


class TestDrawingConstellation(unittest.TestCase):

    def testadddrawingconstellation(self):
        drawingconstellation = DrawingConstellation()
        drawingconstellation.connected_Star = 12
        dbdrawingconstellation = DbDrawingConstellation(drawingconstellation)
        self.assertIsNotNone(dbdrawingconstellation.add_entity())

    def testgetdrawingconstellation(self):
        drawingconstellation = DbDrawingConstellation()
        res = drawingconstellation.get_all()
        self.assertIsNotNone(res)
