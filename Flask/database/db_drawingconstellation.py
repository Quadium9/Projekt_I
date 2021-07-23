from database.db import DB
from models.orm import DrawingConstellation


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
        except Exception:
            self.util.session_rollback()
            raise Exception

    def get(self, id_sel):
        try:
            return self.util.get_session().query(DrawingConstellation).get(id_sel)
        except Exception:
            self.util.session_rollback()
            raise Exception

    def update_entity(self, ids):
        pass

    def delete_id(self, e_id):
        pass

    def returnlist(self, id_star):
        list = []
        for instance in self.util.get_session().query(DrawingConstellation).order_by(DrawingConstellation.connected_Star):
            if instance.connected_Star == id_star:
                list.append(instance)
        return list

