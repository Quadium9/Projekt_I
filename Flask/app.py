import base64
import common.encryption as enc
import flask
import sqlalchemy.exc
from flask import Flask, jsonify, request
from database.db_stars import DBStars, Stars
from flask_cors import cross_origin
from database.db_user import DbUser, User
from database.db_constelations import DBConstellations

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = b'\xaa\x89u\xf7M\xf03\xcb\x1b\xc6#\xd2"\x8b\xf8\xb7'


@app.route('/update-user', methods=['POST'])
@cross_origin()
def update_user():
    try:
        tmp = flask.request.json
        user = DbUser().get_one_by_name(tmp["username"])
        if user.password == str(tmp["passwordold"]):
            user = DbUser().update_entity(tmp, 'change')
            if user:
                return jsonify({'result': True, 'message': 'Dane logowania zostały zmienione'})
            else:
                return jsonify({'result': False, 'message': 'Błąd podczas zmiany danych logowania'})
        else:
            return jsonify({'result': False, 'message': 'Niepoprawne hasło'})
    except AttributeError:
        return jsonify({'result': False, 'message': 'Błąd serwera'})


@app.route('/edit-star', methods=['POST'])
@cross_origin()
def edit_star():
    try:
        tmp = flask.request.json
        trueadmin = DbUser().get_one_by_name(tmp['username'])
        if trueadmin.rules != 'administrator':
            return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})

        cons = DBConstellations().get_one_by_name(tmp['constellation'])
        tmp['constellation'] = cons.id
        star = DBStars().update_entity(tmp, "edit")
        if star:
            return jsonify({'result': True, 'message': 'Dane gwiazdy został zmienione'})
        return jsonify({'result': False, 'message': 'Błąd edycji gwiazdy'})
    except AttributeError:
        return jsonify({'result': False, 'message': 'Błąd w parametrach gwiazdy'})


@app.route('/confirmed-star/<id>/<username>', methods=['GET'])
@cross_origin()
def confirmed_star(id, username):
    try:
        if request.method == 'GET':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})

            if DBStars().update_entity(id, "confirm"):
                return jsonify({'result': True, 'message': 'Gwiazda została potwierdzona'})
            return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})

    except AttributeError:
        return jsonify({'result': False, 'message': 'Błąd potwierdzenia gwiazdy'})


@app.route('/delete-star/<username>', methods=['POST'])
@cross_origin()
def delete_star(username):
    try:
        if request.method == 'POST':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})

            tmp = flask.request.json
            star = DBStars().delete_id(tmp['id'])
            if star:
                return jsonify({'result': True, 'message': "Usunięto gwiazdę " + tmp['name']})
            return jsonify({'result': False, 'message': "Błąd usuwania gwiazdy"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Błąd usuwania gwiazdy"})


@app.route('/form-list-admin-NO/<username>', methods=['GET'])
@cross_origin()
def form_list_admin_NO(username):
    try:
        if request.method == 'GET':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            stars = DBStars().get_all()
            j = []
            for s in stars:
                if s.confirmed == "NO":
                    if s.discaverer == None:
                        disn = "Nie przypisano"
                        disl = ""
                    else:
                        disn = str(s.discaverer.name)
                        disl = str(s.discaverer.surname)
                    j.append({'id': str(s.id),
                              'confirmed': str(s.confirmed),
                              'name': str(s.name),
                              'rectascensionh': str(s.rectascensionh),
                              'rectascensionm': str(s.rectascensionm),
                              'rectascensions': str(s.rectascensions),
                              'declinationh': str(s.declinationh),
                              'declinationm': str(s.declinationm),
                              'declinations': str(s.declinations),
                              'radial_speed': str(s.radial_speed),
                              'distance': str(s.distance),
                              'brightness': str(s.brightness),
                              'star_type': str(s.star_type),
                              'mass': str(s.mass),
                              'greek_symbol': str(s.greek_symbol),
                              'discaverer_name': disn,
                              'discaverer_lastname': disl,
                              'constellation_name': str(s.constellation.name),
                              })
            return jsonify(j)
    except TypeError:
        return jsonify({'result': False, 'message': "Błąd pobierania"})


@app.route('/form-list-admin-YES/<username>', methods=['GET'])
@cross_origin()
def form_list_admin_YES(username):
    try:
        if request.method == 'GET':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            stars = DBStars().get_all()
            j = []
            for s in stars:
                if s.confirmed == "YES":
                    if s.discaverer == None:
                        disn = "Nie przypisano"
                        disl = ""
                    else:
                        disn = str(s.discaverer.name)
                        disl = str(s.discaverer.surname)
                    j.append({'id': str(s.id),
                              'confirmed': str(s.confirmed),
                              'name': str(s.name),
                              'rectascensionh': str(s.rectascensionh),
                              'rectascensionm': str(s.rectascensionm),
                              'rectascensions': str(s.rectascensions),
                              'declinationh': str(s.declinationh),
                              'declinationm': str(s.declinationm),
                              'declinations': str(s.declinations),
                              'radial_speed': str(s.radial_speed),
                              'distance': str(s.distance),
                              'brightness': str(s.brightness),
                              'star_type': str(s.star_type),
                              'mass': str(s.mass),
                              'greek_symbol': str(s.greek_symbol),
                              'discaverer_name': disn,
                              'discaverer_lastname': disl,
                              'constellation_name': str(s.constellation.name),
                              })
            return jsonify(j)
        return jsonify({'result': False, 'message': "Błąd pobierania"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Błąd pobierania"})


@app.route('/user-to-admin/<username>', methods=['POST'])
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


@app.route('/admin-to-user/<username>', methods=['POST'])
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


@app.route('/get-all-user', methods=['GET'])
@cross_origin()
def get_all_user():
    try:
        if request.method == 'GET':
            user = DbUser().get_all()
            j = []
            for u in user:
                j.append({
                    'id': str(u.id),
                    'username': str(u.login),
                    'firstname': str(u.name),
                    'lastname': str(u.surname),
                    'email': str(u.email),
                    'rules': str(u.rules)
                })
            return jsonify(j)
        return jsonify({'result': False, 'message': "Błąd pobierania"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Błąd pobierania"})


@app.route('/login-system', methods=['POST'])
@cross_origin()
def user_login():
    try:
        if request.method == 'POST':
            tmp = flask.request.json
            user = DbUser().get_one_by_name(tmp["username"])
            j = []
            if enc.comparepassword(tmp["password"], user.password):
                j.append({
                    'result': True,
                    'id': user.id,
                    'firstname': str(user.name),
                    'lastname': str(user.surname),
                    'username': str(user.login),
                    'password': str(user.password),
                    'email': str(user.email),
                    'rules': str(user.rules)
                })
                return jsonify(j)
            else:
                return jsonify({'result': False, 'message': "Niepoprawne hasło lub nazwa użytkownika"})
    except AttributeError:
        return jsonify({'id': None, 'message': "Niepoprawne dane logowania"})


@app.route('/register-user', methods=['POST'])
@cross_origin()
def register_user():
    try:
        if request.method == 'POST':
            tmp = flask.request.json
            user = User()
            user.name = tmp['firstname']
            user.surname = tmp['lastname']
            user.login = tmp['username']
            password = enc.createhash(tmp['password'])
            user.password = str(password)
            user.email = tmp['email']
            user.rules = 'użytkownik'
            new_user = DbUser(user).add_entity()
            j = ({'id': new_user})
            return jsonify(j)
    except sqlalchemy.exc.IntegrityError:
        return jsonify(({'id': None, 'message': "Nazwa użytkownika lub email już istnieje"}))


@app.route('/add_new_star/<username>', methods=['POST'])
@cross_origin()
def add_new_star(username):
    try:
        if request.method == 'POST':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            tmp = flask.request.json
            star = Stars()
            cons = DBConstellations().get_one_by_name(tmp['constellation'])
            star.name = tmp['name']
            if tmp['rectascensionh'] > 60 or tmp['rectascensionm'] > 60 or tmp['rectascensions'] > 60:
                return jsonify({'result': False, 'message': "Rektascencja nie może przekroczyć 60"})
            if tmp['declinationh'] > 60 or tmp['declinationm'] > 60 or tmp['declinations'] > 60:
                return jsonify({'result': False, 'message': "Deklinacja nie może przekroczyć 60"})
            star.rectascensionh = tmp['rectascensionh']
            star.rectascensionm = tmp['rectascensionm']
            star.rectascensions = tmp['rectascensions']
            star.declinationh = tmp['declinationh']
            star.declinationm = tmp['declinationm']
            star.declinations = tmp['declinations']
            star.constelation_id = cons.id
            star.discaverer_id = tmp['discavererid']
            star.star_type = tmp['star_type']
            star.radial_speed = tmp['radial_speed']
            star.distance = tmp['distance']
            star.brightness = tmp['brightness']
            star.mass = tmp['mass']
            star.greek_symboxl = None
            star.confirmed = "NO"
            DBStars(star).add_entity()
            return jsonify({'result': True, 'message': "Wysłano formularz"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Podany gwiazdozbiór nie istnieje w bazie"})


@app.route('/get_star_by_name/<star_name>', methods=['GET'])
@cross_origin()
def get_star_by_name(star_name):
    try:
        stars = DBStars().get_one_by_name(star_name)
        j = []
        if star_name is None:
            return jsonify({'result': False, 'message': "Proszę wpisać nazwę"})
        for s in stars:
            if s.confirmed == "YES":
                if s.discaverer is None:
                    j.append({'id': str(s.id),
                              'confirmed': str(s.confirmed),
                              'name': str(s.name),
                              'rectascensionh': str(s.rectascensionh),
                              'rectascensionm': str(s.rectascensionm),
                              'rectascensions': str(s.rectascensions),
                              'declinationh': str(s.declinationh),
                              'declinationm': str(s.declinationm),
                              'declinations': str(s.declinations),
                              'radial_speed': str(s.radial_speed),
                              'distance': str(s.distance),
                              'brightness': str(s.brightness),
                              'star_type': str(s.star_type),
                              'mass': str(s.mass),
                              'greek_symbol': str(s.greek_symbol),
                              'discaverer_name': "Nie przypisano",
                              'discaverer_lastname': "",
                              'constellation_name': str(s.constellation.name),
                              'picture': str(s.constellation.name + s.constellation.picture),
                              })
                else:
                    j.append({'id': str(s.id),
                              'confirmed': str(s.confirmed),
                              'name': str(s.name),
                              'rectascensionh': str(s.rectascensionh),
                              'rectascensionm': str(s.rectascensionm),
                              'rectascensions': str(s.rectascensions),
                              'declinationh': str(s.declinationh),
                              'declinationm': str(s.declinationm),
                              'declinations': str(s.declinations),
                              'radial_speed': str(s.radial_speed),
                              'distance': str(s.distance),
                              'brightness': str(s.brightness),
                              'star_type': str(s.star_type),
                              'mass': str(s.mass),
                              'greek_symbol': s.greek_symbol,
                              'discaverer_name': s.discaverer.name,
                              'discaverer_lastname': s.discaverer.surname,
                              'constellation_name': s.constellation.name,
                              'picture': str(s.constellation.name + s.constellation.picture),
                              })
            if len(j) >= 25:
                 break
        return jsonify(j)
    except TypeError:
        return jsonify({'result': False, 'message': "Błąd nazwy gwiazdy"})


@app.route('/get_star_by_constellation/<constellation>', methods=['GET'])
@cross_origin()
def get_star_by_constellation(constellation):
    try:
        star = DBStars().get_all()
        j = []
        for s in star:
            if s.constellation.name == constellation:
                if s.confirmed == "YES":
                    if s.discaverer is None:
                        j.append({'id': str(s.id),
                                  'confirmed': str(s.confirmed),
                                  'name': str(s.name),
                                  'rectascensionh': str(s.rectascensionh),
                                  'rectascensionm': str(s.rectascensionm),
                                  'rectascensions': str(s.rectascensions),
                                  'declinationh': str(s.declinationh),
                                  'declinationm': str(s.declinationm),
                                  'declinations': str(s.declinations),
                                  'radial_speed': str(s.radial_speed),
                                  'distance': str(s.distance),
                                  'brightness': str(s.brightness),
                                  'star_type': str(s.star_type),
                                  'mass': str(s.mass),
                                  'greek_symbol': str(s.greek_symbol),
                                  'discaverer_name': "Nie przypisano",
                                  'discaverer_lastname': "",
                                  'constellation_name': str(s.constellation.name),
                                  'picture': str(s.constellation.name + s.constellation.picture),
                                  })
                    else:
                        j.append({'id': str(s.id),
                                  'confirmed': str(s.confirmed),
                                  'name': str(s.name),
                                  'rectascensionh': str(s.rectascensionh),
                                  'rectascensionm': str(s.rectascensionm),
                                  'rectascensions': str(s.rectascensions),
                                  'declinationh': str(s.declinationh),
                                  'declinationm': str(s.declinationm),
                                  'declinations': str(s.declinations),
                                  'radial_speed': str(s.radial_speed),
                                  'distance': str(s.distance),
                                  'brightness': str(s.brightness),
                                  'star_type': str(s.star_type),
                                  'mass': str(s.mass),
                                  'greek_symbol': s.greek_symbol,
                                  'discaverer_name': s.discaverer.name,
                                  'discaverer_lastname': s.discaverer.surname,
                                  'constellation_name': s.constellation.name,
                                  'picture': str(s.constellation.name + s.constellation.picture),
                                  })
        return jsonify(j)
    except:
        return jsonify({'result': False, 'message': 'Bład pobierania danych.'})


@app.route('/all-constellations', methods=['GET'])
@cross_origin()
def all_constellations():
    try:
        if request.method == 'GET':
            constellations = DBConstellations().get_all()
            j = []
            for c in constellations:
                j.append({
                    'id': str(c.id),
                    'name': str(c.name),
                    'declination': str(c.declination),
                    'rectascension': str(c.rectascension),
                    'symbolism': str(c.symbolism),
                    'sky_side': str(c.sky_side),
                    'area': str(c.area),
                    'picture': str(c.picture)
                })
            return jsonify(j)
        return jsonify({'result': False, 'message': 'Bład pobierania gwiazdozbiorów'})
    except AttributeError:
        return jsonify({'result': False, 'message': 'Błąd danych'})


@app.route('/constellation_image/<constellation_id>', methods=['GET'])
@cross_origin()
def constellation_image(constellation_id):
    c = DBConstellations().get(constellation_id)
    star = DBStars().get_all()
    number_of_star = 0
    for s in star:
        if c.name == s.constellation.name:
            number_of_star = number_of_star + 1
    j = ({
        'id': c.id,
        'picture': str(c.name + c.picture),
        'star_number': number_of_star
    })
    return jsonify(j)


@app.route('/get_one_star/<star_id>', methods=['GET'])
@cross_origin()
def get_one_star(star_id):
    s = DBStars().get(star_id)
    j = ({'id': str(s.id),
          'name': str(s.name),
          'rectascensionh': str(s.rectascensionh),
          'rectascensionm': str(s.rectascensionm),
          'rectascensions': str(s.rectascensions),
          'declinationh': str(s.declinationh),
          'declinationm': str(s.declinationm),
          'declinations': str(s.declinations),
          'radial_speed': str(s.radial_speed),
          'distance': str(s.distance),
          'brightness': str(s.brightness),
          'star_type': str(s.star_type),
          'mass': str(s.mass),
          'greek_symbol': str(s.greek_symbol),
          'discaverer_name': str(s.discaverer.name),
          'constellation_name': str(s.constellation.name)})
    return jsonify(j)


if __name__ == '__main__':
    app.run()
