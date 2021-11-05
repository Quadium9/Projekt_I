import common.validation as cv
from .db import DB
from flask import Response
from models.orm import User


class DbUser(DB):

    def __init__(self, user=User.__class__):
        super().__init__()
        self.user = user

    def get_all(self):
        try:
            return self.util.get_session().query(User).all()
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

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
            return Response('Server has found an error in database', 500, mimetype='application/json')

    def get_one_by_name(self, name):
        try:
            return self.util.get_session().query(User).filter(User.login == name).first()
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def get(self, id_sel):
        try:
            return self.util.get_session().query(User).get(id_sel)
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def update_entity(self, ids, option):
        try:
            if option == 'rules':
                self.util.get_session().query(User).filter(User.id == ids['id']).update({User.rules: ids['rules']},
                                                                                    synchronize_session=False)

            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def delete_id(self, ide):
        try:
            self.util.get_session().query(User).filter(User.id == ide).delete()
            self.util.get_session().commit()
            return True
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')
