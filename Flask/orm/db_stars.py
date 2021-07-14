from .db import DB
from orm import Stars


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
            self.util.get_session().add(self.stars)
            self.util.get_session().comit()
            return True
        except Exception:
            self.util.session_rollback()
            raise Exception

    def get(self, id_sel):
        try:
            return self.util.get_session().query(Stars).get(id_sel)
        except Exception:
            self.util.session_rollback()
            raise Exception

    def update_entity(self, ids):
        pass

    def delete_id(self, e_id):
        pass
