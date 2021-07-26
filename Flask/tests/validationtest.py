import common.validation
from models.orm import *
from database.db_drawingconstellation import DbDrawingConstellation
from database.db_planet import DBPlanet
from database.db_stars import DBStars
from database.db_user import DbUser
from database.db_constelations import DBConstellations

import unittest


class TestMetthods(unittest.TestCase):

    def testvalidationnumber(self):
        draw = DrawingConstellation()
        draw.connected_Star = 3
        if common.validation.validate_text(draw.connected_Star):
            drawing = DbDrawingConstellation(draw)
            drawing.add_entity()
            return True
        return False

    def testvalidationonecharnegative(self):
        stars = Stars()
        stars.greek_symbol = 'ce'
        self.assertFalse(common.validation.onechar_text(stars.greek_symbol))

    def testvalidationpasswordnegative(self):
        user = User()
        user.password = "1234567"
        self.assertFalse(common.validation.password_validation(user.password))

    def testvalidationemailnegative(self):
        user = User()
        user.email = "test@test"
        self.assertFalse(common.validation.email_validation(user.email))


