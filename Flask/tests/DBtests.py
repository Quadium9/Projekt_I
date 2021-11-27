from models.orm import *
from database.db_stars import DBStars
from database.db_user import DbUser
from database.db_constelations import DBConstellations
from common import stars_type, validation
import unittest
import common.encryption as enc


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


class ValidationTest(unittest.TestCase):

    def testvalidation(self):
        res = validation.validationNone("")
        print(res)

    def testcreatehash(self):
        result = enc.createhash('admin_token')
        print(result)

    def testcomparehash(self):
        create = b'\x9a?\xa3\xba\x89Gc,#2\xa4\xf0\x8e\xdb\xd4\xb9\xa3N\x16\x81\xd5\x95\x1a\xeb\x19\xc2\xe8|E\xa3\x10\xae\x01\xc5B\x1a\x83,\xb1ds\x0f\x10%\xf7\x173\xd9O\xe7\x1a\x95C\xd9\x96\x18\x8d^u/\x0f\xb5\xee\xda'
        res = enc.comparepassword('haslo', create)
        print(res)
