import common.validation as cv
from database.db import DB
from flask import Response
from models.orm import User


class DbUser(DB):

    def __init__(self, user=User.__class__):
        super().__init__()
        self.user = user

    def get_all(self):
        try:
            return self.util.get_session().query(User).all()
        except Exception:
            self.util.session_rollback()
            raise Exception

    def get_query(self):
        pass

    def add_entity(self):
        try:
            if cv.email_validation(self.user.email) and cv.password_validation(self.user.password):
                self.util.get_session().add(self.user)
                self.util.get_session().commit()
                return self.user.id
            return None
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def get(self, id_sel):
        try:
            print(self.util.get_session().query(User).get(id_sel))
            return self.util.get_session().query(User).get(id_sel)
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def update_entity(self, ids):
        pass

    def update_name_surname_email(self, ids, name, surname, email):
        try:
            if cv.email_validation(email) and name is not None and surname is not None:
                self.util.get_session().query(User).filter(User.id == ids).update({User.name: name,
                     User.surname: surname, User.email: email})
                self.util.get_session().commit()
                return True
            return False
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def update_password(self, ids, password):
        try:
            if cv.password_validation(password):
                self.util.get_session().query(User).filter(User.id == ids).update({User.password: password})
                self.util.get_session().commit()
                return True
            return False
        except Response:
            self.util.session_rollback()
            return Response('message', 200, mimetype='application/json')

    def delete_id(self, ide):
        try:
            self.util.get_session().query(User).filter(User.id == ide).delete()
            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            raise Response('massage', 200, mimetype='application/json')
