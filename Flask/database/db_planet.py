from .db import DB
from flask import Response
from models.orm import Planet
from Exceptions import Exceptions


class DBPlanet(DB):

    def __init__(self, planet=Planet.__class__):
        super().__init__()
        self.planet = planet

    def get_all(self):
        try:
            return self.util.get_session().query(Planet).all()
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetyoe='application/json')

    def get_query(self):
        pass

    def add_entity(self):
        try:
            if self.planet.name is not None:
                self.util.get_session().add(self.planet)
                self.util.get_session().commit()
                return self.planet.id
            raise Exceptions.ExceptionNone
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetyoe='application/json')

    def get(self, id_sel):
        try:
            return self.util.get_session().query(Planet).get(id_sel)
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetyoe='application/json')

    def update_entity(self, ids):
        try:
            if self.planet.name is not None:
                self.util.get_session().query(Planet).filter(Planet.id == ids).update({Planet.name: self.planet.name,
                                                                                       Planet.id_star: self.planet.id_star})
                self.util.get_session().commit()
                return True
            return Exceptions.ExceptionNone
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetyoe='application/json')

    def delete_id(self, e_id):
        try:
            self.util.get_session().query(Planet).filter(Planet.id == e_id).delete()
            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype="application/json")
