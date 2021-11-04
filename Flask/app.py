import flask
import pymysql.err
import sqlalchemy.exc
from flask import Flask, jsonify, request
from flask_cors import cross_origin
from database.db_stars import DBStars, Stars
from database.db_user import DbUser, User
from database.db_drawingconstellation import DrawingConstellation, DbDrawingConstellation
from database.db_planet import DBPlanet, Planet
from database.db_constelations import DBConstellations, Constellations

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = b'\xaa\x89u\xf7M\xf03\xcb\x1b\xc6#\xd2"\x8b\xf8\xb7'


@app.route('/login-system', methods=['POST'])
@cross_origin()
def user_login():
    try:
        if request.method == 'POST':
            tmp = flask.request.json
            user = DbUser().get_one_by_name(tmp["username"])
            j = []
            if user.password == tmp["password"]:
                j.append({
                    'id': str(user.id),
                    'firstname': str(user.name),
                    'lastname': str(user.surname),
                    'username': str(user.login),
                    'password': str(user.password),
                    'email': str(user.email),
                    'rules': str(user.rules)
                })
                return jsonify(j)
            return jsonify({'id': None, 'message': "Niepoparwne hasło"})
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
            user.password = tmp['password']
            user.email = tmp['email']
            user.rules = 'user'
            new_user = DbUser(user).add_entity()
            j = ({'id': new_user})
            return jsonify(j)
    except sqlalchemy.exc.IntegrityError as e:
        return jsonify(({'id': None, 'message': "Nazwa użytkownika lub email już istnieje"}))


@app.route('/add_new_star', methods=['POST'])
@cross_origin()
def add_new_star():
    try:
        if request.method == 'POST':
            tmp = flask.request.json
            star = Stars()
            cons = DBConstellations().get_one_by_name(tmp['constellation'])
            star.name = tmp['name']
            star.rectascension = tmp['rectascension']
            star.declination = tmp['declination']
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
            return jsonify({'message': "Wysłano formularz"})
    except AttributeError:
        return jsonify({'message': "Podany gwiazdozbiór nie istnieje w bazie"})


@app.route('/get_one_star_by_name/<star_name>', methods=['GET'])
@cross_origin()
def get_one_star_by_name(star_name):
    try:
        stars = DBStars().get_one_by_name(star_name)
        j = []
        for s in stars:
            if s.confirmed == "YES":
                j.append({'id': str(s.id),
                          'confirmed': str(s.confirmed),
                          'name': str(s.name),
                          'rectascension': str(s.rectascension),
                          'declination': str(s.declination),
                          'radial_speed': str(s.radial_speed),
                          'distance': str(s.distance),
                          'brightness': str(s.brightness),
                          'star_type': str(s.star_type),
                          'mass': str(s.mass),
                          'greek_symbol': str(s.greek_symbol),
                          'discaverer_name': str(s.discaverer.name),
                          'discaverer_lastname': str(s.discaverer.surname),
                          'constellation_name': str(s.constellation.name),
                          })
        return jsonify(j)
    except TypeError:
        return jsonify({None})


@app.route('/data-for-image/<id_cons>', methods=['GET'])
@cross_origin()
def data_for_image(id_cons):
    c = DbDrawingConstellation().get_one_by_name(id_cons)
    j = []
    for dc in c:
        j.append({
            'id': str(dc.id),
            'star_name_in': str(dc.star_name_in),
            'star_name_out': str(dc.star_name_out)
        })
    return jsonify(j)


@app.route('/to-jsonC', methods=['GET'])
@cross_origin()
def to_jsonC():
    constellations = DBConstellations().get_all()

    j = []
    for c in constellations:
        j.append({
            'id': str(c.id),
            'name': str(c.name),
            'declination': str(c.declination),
            'symbolism': str(c.symbolism),
            'sky_side': str(c.sky_side),
            'area': str(c.area)
        })
    return jsonify(j)


@app.route('/get_one_star/<star_id>', methods=['GET'])
@cross_origin()
def get_one_star(star_id):
    s = DBStars().get(star_id)
    j = ({'id': str(s.id),
          'name': str(s.name),
          'rectascension': str(s.rectascension),
          'declination': str(s.declination),
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
