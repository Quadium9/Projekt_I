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
        except Exception:
            self.util.session_rollback()
            raise Exception

    def get_query(self):
        pass

    def add_entity(self):
        try:
            self.util.get_session().add(self.drawing)
            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def get(self, id_sel):
        try:
            return self.util.get_session().query(DrawingConstellation).get(id_sel)
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def update_entity(self, ids, connectedstar):
        try:
            if self.drawing.connected_Star is not None:
                self.util.get_session().query(DrawingConstellation).filter(DrawingConstellation.id == ids).\
                    update({DrawingConstellation.connected_Star: connectedstar})
                return True
            return False
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def delete_id(self, e_id):
        try:
            if self.drawing.connected_Star is not None:
                self.util.get_session().query(DrawingConstellation).filter(DrawingConstellation.id == e_id).delete()
                self.util.get_session().commit()
                return True
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def returnlist(self, id_star):
        list = []
        for instance in self.util.get_session().query(DrawingConstellation).order_by(DrawingConstellation.connected_Star):
            if instance.connected_Star == id_star:
                list.append(instance)
        return list

