import common.encryption as enc
import common.validation as val
import flask
import sqlalchemy.exc
from flask import jsonify, request, Blueprint
from flask_cors import cross_origin
from database.db_user import DbUser, User

user_api = Blueprint('/user', __name__)


@user_api.route('/get-user-by-name/<name>/<loged>', methods=['GET'])
@cross_origin()
def get_user_by_name(name, loged):
    try:
        search_value = "%{}%".format(name)
        user = DbUser().get_query().filter(User.login.like(search_value)).all()
        trueadmin = DbUser().get_one_by_name(loged)
        if trueadmin is None:
            return jsonify({'result': False, 'message': 'Proszę się zalogować'})
        if trueadmin.rules != 'administrator':
            return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
        if user is None:
            return jsonify({'result': False, 'message': 'Podany użytkownik nie istnieje'})
        j = []
        for u in user:
            if u is None:
                return jsonify(j)
            j.append({
                'id': u.id,
                'username': u.login,
                'firstname': u.name,
                'lastname': u.surname,
                'email': u.email,
                'star_number': u.star_number,
                'rules': u.rules
            })
        return jsonify(j)
    except:
        return jsonify({'result': False, 'message': 'Błąd serwera'})


@user_api.route('/update-user', methods=['POST'])
@cross_origin()
def update_user():
    try:
        tmp = flask.request.json
        user = DbUser().get_one_by_name(tmp["username"])
        if enc.comparepassword(str(tmp["passwordold"]), user.password):
            new_pass = enc.createhash(str(tmp["passwordnew"]))
            user = DbUser().update_entity(new_pass, 'change')
            if user:
                return jsonify({'result': True, 'message': 'Dane logowania zostały zmienione'})
            else:
                return jsonify({'result': False, 'message': 'Błąd podczas zmiany danych logowania'})
        else:
            return jsonify({'result': False, 'message': 'Niepoprawne hasło'})
    except AttributeError:
        return jsonify({'result': False, 'message': 'Błąd serwera'})


@user_api.route('/user-to-admin/<username>', methods=['POST'])
@cross_origin()
def user_to_admin(username):
    try:
        if request.method == 'POST':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            tmp = flask.request.json
            tmp['rules'] = 'administrator'
            user = DbUser().update_entity(tmp, 'rules')
            if user:
                return jsonify({'result': True, 'message': "Użytkownik " + tmp['username'] + " został administratorem"})
        return jsonify({'result': False, 'message': 'Błąd zmiany uprawnień'})
    except AttributeError:
        return jsonify({'result': False, 'message': 'Niepoprawne dane'})


@user_api.route('/admin-to-user/<username>', methods=['POST'])
@cross_origin()
def admin_to_user(username):
    try:
        if request.method == 'POST':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            tmp = flask.request.json
            tmp['rules'] = 'użytkownik'
            user = DbUser().update_entity(tmp, 'rules')
            if user:
                return jsonify(
                    {'result': True, 'message': "Administrator " + tmp['username'] + " został użytkownikiem"})
        return jsonify({'result': False, 'message': 'Błąd zmiany uprawnień'})
    except AttributeError:
        return jsonify({'result': False, 'message': 'Niepoprawne dane'})


@user_api.route('/get-all-user/<username>/<nrpage>', methods=['GET'])
@cross_origin()
def get_all_user(username, nrpage):
    try:
        if request.method == 'GET':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            query = DbUser().get_query()
            if int(nrpage) <= 0:
                return jsonify({'result': False, 'message': "Numer strony nie może być ujemny"})
            items = query.limit(25).offset((int(nrpage) - 1) * 25).all()
            j = []
            for ut in items:
                u = DbUser().get(ut.id)
                if u is None:
                    return jsonify(j)
                j.append({
                    'id': str(u.id),
                    'username': str(u.login),
                    'firstname': str(u.name),
                    'lastname': str(u.surname),
                    'email': str(u.email),
                    'rules': str(u.rules),
                    'star_number': u.star_number
                })
            return jsonify(j)
        return jsonify({'result': False, 'message': "Błąd pobierania"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Błąd pobierania"})


@user_api.route('/login-system', methods=['POST'])
@cross_origin()
def user_login():
    try:
        if request.method == 'POST':
            tmp = flask.request.json
            user = DbUser().get_one_by_name(tmp["username"])
            j = []
            if enc.comparepassword(str(tmp["password"]), user.password):
                j.append({
                    'result': True,
                    'id': user.id,
                    'firstname': str(user.name),
                    'lastname': str(user.surname),
                    'username': str(user.login),
                    'password': str(user.password),
                    'email': str(user.email),
                    'rules': str(user.rules),
                    'star_number': user.star_number
                })
                return jsonify(j)
            else:
                return jsonify({'result': False, 'message': "Niepoprawne hasło lub nazwa użytkownika"})
        return jsonify({'result': False, 'message': "Niepoprawny format danych"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Niepoprawne dane logowania"})


@user_api.route('/register-user', methods=['POST'])
@cross_origin()
def register_user():
    try:
        if request.method == 'POST':
            tmp = flask.request.json
            user = User()
            sUser = DbUser().get_one_by_name(tmp['username'])
            if sUser is not None:
                if sUser.login == tmp['username']:
                    return jsonify({'result': False, 'message': 'Użytkownik o podanej nazwie już istnieje'})
                if sUser.email == tmp['email']:
                    return jsonify({'result': False, 'message': 'Podany email juz istnieje'})
            if val.validate_text(str(tmp['firstname'])) or val.validate_text(str(tmp['lastname'])):
                return jsonify({'result': False, 'message': 'Imie i nazwisko nie mogą zawierać cyfr'})
            if not val.email_validation(str(tmp['email'])):
                return jsonify({'result': False, 'message': 'Email jest niepoprawny'})
            user.name = tmp['firstname']
            user.surname = tmp['lastname']
            user.login = tmp['username']
            password = enc.createhash(str(tmp['password']))
            user.password = str(password)
            user.email = tmp['email']
            user.star_number = 0
            user.rules = 'użytkownik'
            new_user = DbUser(user).add_entity()
            j = ({'id': new_user})
            return jsonify(j)
    except sqlalchemy.exc.IntegrityError:
        return jsonify(({'result': False, 'message': "Nazwa użytkownika lub email już istnieje"}))
