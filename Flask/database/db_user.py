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
        try:
            return self.util.get_session().query(User)
        except Response:
            self.util.session_rollback()
            raise Response('Server has found an error in database', 500, mimetype='application/json')

    def add_entity(self):
        try:
            if cv.validationNone(self.user.password) and cv.validationNone(self.user.login) \
                    and cv.validationNone(self.user.email) and cv.validationNone(self.user.surname) \
                    and cv.validationNone(self.user.name):
                self.util.get_session().add(self.user)
                self.util.get_session().commit()
                return self.user.id
            return False
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
            if option == 'change':
                if cv.validationNone(str(ids['username'])) and cv.validationNone(str(ids['passwordnew'])) \
                        and len(str(ids['passwordnew'])) >= 8:
                    self.util.get_session().query(User).filter(User.id == ids['id']).update({
                        User.login: ids['username'],
                        User.password: ids['passwordnew']
                    }, synchronize_session=False)
                    self.util.get_session().commit()
                    return True
            if option == 'levelup':
                self.util.get_session().query(User).filter(User.id == ids['id']).update({
                    User.star_number: int(ids['star_number'])
                }, synchronize_session=False)
                self.util.get_session().commit()
                return True
            return False
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
