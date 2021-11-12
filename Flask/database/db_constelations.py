from .db import DB
from models.orm import Constellations
from flask import Response


class DBConstellations(DB):

    def __init__(self, constellations=Constellations.__class__):
        super().__init__()
        self.constellations = constellations

    def get_all(self):
        try:
            return self.util.get_session().query(Constellations).all()
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get_query(self):
        pass

    def add_entity(self):
        try:
            if self.constellations.name is not None:
                self.util.get_session().add(self.constellations)
                self.util.get_session().commit()
                return self.constellations.id
            return False
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetype='application/json')

    def get(self, id_sel):
        try:
            return self.util.get_session().query(Constellations).get(id_sel)
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get_one_by_name(self, name):
        try:
            search_value = "%{}%".format(name)
            return self.util.get_session().query(Constellations).filter(Constellations.name.like(search_value)).first()
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetype='application/json')

    def update_entity(self, ids, option):
        pass

    def delete_id(self, e_id):
        try:
            self.util.get_session().query(Constellations).filter(Constellations.id == e_id).delete()
            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get_login(self, login, password):
        return False
