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


@app.route('/all_stars', methods=['GET'])
def to_jsonS():
    stars = DBStars().get_all()
    j = []
    for s in stars:
        j.append({
            'id': str(s.id),
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
            'constellation_name': str(s.constellation.name),
        })
    return jsonify(j)


@app.route('/add_new_star', methods=['GET', 'POST'])
def add_new_star():
    if request.method == 'POST':
        name = request.form.get('name')
        rectascension = request.form.get('rectascension')
        declination = request.form.get('declination')
        radial_speed = request.form.get('radial_speed')
        distance = request.form.get('distance')
        brightness = request.form.get('brightness')
        mass = request.form.get('mass')
        greek_symbol = request.form.get('greek_symbol')
        star_type = request.form.get('star_type')
        constellation_id = request.form.get('constellation_id')
        new_star = Stars(name, rectascension, declination, radial_speed, distance, brightness, mass,
                         star_type, constellation_id, greek_symbol)
        DBStars(new_star).add_entity()
        return jsonify(new_star)


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


@app.route('/get_one_star_by_name/<star_name>', methods=['GET'])
@cross_origin()
def get_one_star_by_name(star_name):
    stars = DBStars().get_one_by_name(star_name)
    j = []
    for s in stars:
        j.append({'id': str(s.id),
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


@app.route('/to-jsonP', methods=['GET'])
def to_jsonP():
    planet = DBPlanet().get_all()
    j = []
    for p in planet:
        j.append({
            'name': p.name,
            'id_star': p.star.name
        })


@app.route('/login-system', methods=['GET'])
@cross_origin()
def user_data():
    user_login = request.args.get('user-login')
    user_password = request.args.get('user-password')
    user = DbUser.get_login(user_login, user_password)
    return user


if __name__ == '__main__':
    app.run()
