from .db import DB
from models.orm import Stars
from flask import Response
from common import validation
from Exceptions import Exceptions
class DBStars(DB):

    def __init__(self, stars=Stars.__class__):
        super().__init__()
        self.stars = stars

    def get_all(self):
        try:
            # qu = self.util.get_session().query(Stars).slice(nrpage * 5, nrpage * 5 + 5)
            # cur = self.util.get_session().execute(qu).fetchall()
            # return cur
            return self.util.get_session().query(Stars).all()
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get_query(self):
        try:
            return self.util.get_session().query(Stars)
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def add_entity(self):
        try:
            if validation.validationNone([self.stars.name, self.stars.rectascensionh,
                                          self.stars.rectascensionm, self.stars.rectascensions,
                                          self.stars.declinationh, self.stars.declinationm, self.stars.declinations]):
                if validation.validate_text(self.stars.mass) and validation.validate_text(self.stars.brightness)\
                        and validation.validate_text(self.stars.distance) and validation.validate_text(self.stars.radial_speed):
                    self.util.get_session().add(self.stars)
                    self.util.get_session().commit()
                    return self.stars
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
                search_value = "%{}%".format(name)
                return self.util.get_session().query(Stars).filter(Stars.name.like(search_value)).all()
            else:
                raise Exceptions.ExceptionNone
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def update_entity(self, ids, option):
        try:
            if option == 'confirm':
                self.util.get_session().query(Stars).filter(Stars.id == ids).update({Stars.confirmed: "YES"}, synchronize_session=False)
                self.util.get_session().commit()
                return True
            else:
                if option == 'edit':
                    if validation.validationNone([ids['name'], ids['rectascensionh'], ids['rectascensionm'],
                                                  ids['rectascensions'], ids['declinationh'], ids['constellation'],
                                                  ids['declinationm'], ids['declinations']]):

                        self.util.get_session().query(Stars).filter(Stars.id == ids['id']).\
                                                          update({Stars.name: ids['name'],
                                                                  Stars.rectascensionh: ids['rectascensionh'],
                                                                  Stars.rectascensionm: ids['rectascensionm'],
                                                                  Stars.rectascensions: ids['rectascensions'],
                                                                  Stars.declinationh: ids['declinationh'],
                                                                  Stars.declinationm: ids['declinationm'],
                                                                  Stars.declinations: ids['declinations'],
                                                                  Stars.constelation_id: ids['constellation'],
                                                                  Stars.star_type: ids['star_type'],
                                                                  Stars.radial_speed: ids['radial_speed'],
                                                                  Stars.distance: ids['distance'],
                                                                  Stars.brightness: ids['brightness'],
                                                                  Stars.mass: ids['mass'],
                                                                  }, synchronize_session=False)
                        self.util.get_session().commit()
                        return True
            return False
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
