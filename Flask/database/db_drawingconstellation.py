from database.db import DB
from models.orm import DrawingConstellation
from flask import Response


class DbDrawingConstellation(DB):

    def __init__(self, drawing=DrawingConstellation.__class__):
        super().__init__()
        self.drawing = drawing

    def get_all(self):
        try:
            return self.util.get_session().query(DrawingConstellation).all()
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get_query(self):
        pass

    def add_entity(self):
        try:
            self.util.get_session().add(self.drawing)
            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get(self, id_sel):
        try:
            return self.util.get_session().query(DrawingConstellation).filter(DrawingConstellation.constellation_id.like(id_sel)).all()
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def update_entity(self, ids, option):
        pass

    def delete_id(self, e_id):
        try:
            if self.drawing.connected_Star is not None:
                self.util.get_session().query(DrawingConstellation).filter(DrawingConstellation.id == e_id).delete()
                self.util.get_session().commit()
                return True
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetype='application/json')

    def get_one_by_name(self, name):
        try:
            return self.util.get_session().query(DrawingConstellation).filter(DrawingConstellation.star_name_in.like(name)).all()
        except Response:
            self.util.session_rollback()
            return Response('Server has found an error in database', 500, mimetype='application/json')
