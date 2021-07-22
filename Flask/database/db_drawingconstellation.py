from database.db import DB
from models.orm import DrawingConstellation


class DbDrawingConstellation(DB):

    def __init__(self, planet=DrawingConstellation.__class__):
        super().__init__()
        self.planet = planet

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
            self.util.get_session().add(self.planet)
            self.util.get_session().commit()
            return True
        except Exception:
            self.util.session_rollback()
            raise Exception

    def get(self, id_sel):
        pass

    def update_entity(self, ids):
        pass

    def delete_id(self, e_id):
        pass
