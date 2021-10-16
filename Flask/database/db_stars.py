from .db import DB
from models.orm import Stars
from flask import Response, request
from common import validation
from Exceptions import Exceptions


class DBStars(DB):

    def __init__(self, stars=Stars.__class__):
        super().__init__()
        self.stars = stars

    def get_all(self):
        try:
            return self.util.get_session().query(Stars).all()
        except Exception:
            self.util.session_rollback()
            raise Exception

    def get_query(self):
        pass

    def add_entity(self):
        try:
            if validation.validationNone([self.stars.name, self.stars.rectascension, self.stars.declination]):
                if validation.validate_text(self.stars.mass) and validation.validate_text(self.stars.brightness)\
                        and validation.validate_text(self.stars.distance) and validation.validate_text(self.stars.radial_speed):

                    self.util.get_session().add(self.stars)
                    self.util.get_session().commit()
                    return self.stars.id

                raise Exceptions.ExceptionNotNumber
            raise Exceptions.ExceptionNone
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get(self, id_sel):
        try:
            return self.util.get_session().query(Stars).get(id_sel)
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get_one_by_name(self, name):
        try:
            if name is not None:
                return self.util.get_session().query(Stars).filter(Stars.name >= name).all()
            else:
                raise Exceptions.ExceptionNone
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def update_entity(self, ids):
        try:
            if validation.validationNone(([self.stars.name, self.stars.rectascension, self.stars.declination])):
                self.util.get_session().add(self.stars)
                self.util.get_session().commit()
                return True
            return Exceptions.ExceptionNone
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def delete_id(self, e_id):
        try:
            self.util.get_session().query(Stars).filter(Stars.id == e_id).delete()
            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')
