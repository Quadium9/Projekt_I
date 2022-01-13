from flask import jsonify, request, Blueprint
from database.db_stars import DBStars
from flask_cors import cross_origin
from database.db_constelations import DBConstellations

constellation_api = Blueprint('/constellation', __name__)


@constellation_api.route('/all-constellations', methods=['GET'])
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


@constellation_api.route('/constellation_image/<constellation_id>', methods=['GET'])
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
        'picture': str(c.picture),
        'star_number': number_of_star
    })
    return jsonify(j)
