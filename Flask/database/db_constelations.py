from .db import DB
from models.orm import Constellations


class DBConstellations(DB):

    def __init__(self, constellations=Constellations.__class__):
        super().__init__()
        self.constellations = constellations

    def get_all(self):
        try:
            return self.util.get_session().query(Constellations).all()
        except Exception:
            self.util.session_rollback()
            raise Exception

    def get_query(self):
        pass

    def add_entity(self):
        pass

    def get(self, id_sel):
        try:
            return self.util.get_session().query(Constellations).get(id_sel)
        except Exception:
            self.util.session_rollback()
            raise Exception

    def update_entity(self, ids):
        pass

    def delete_id(self, e_id):
        pass
