import flask
import sqlalchemy
from flask import jsonify, request, Blueprint
import common.validation as val
import Exceptions.Exceptions
from database.db_stars import DBStars, Stars
from flask_cors import cross_origin
from database.db_user import DbUser
from database.db_constelations import DBConstellations
from common import stars_type

field = Blueprint('/star', __name__)


@field.route('/delete-star/<username>', methods=['POST'])
@cross_origin()
def delete_star(username):
    try:
        if request.method == 'POST':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            tmp = flask.request.json
            if DBStars().delete_id(tmp['id']):
                ids = {'id': trueadmin.id, 'star_number': int(trueadmin.star_number) - 1}
                if DbUser().update_entity(ids, 'levelup'):
                    return jsonify({'result': True, 'message': "Usunięto gwiazdę " + tmp['name']})
            return jsonify({'result': False, 'message': "Błąd usuwania gwiazdy"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Błąd usuwania gwiazdy"})


@field.route('/edit-star', methods=['POST'])
@cross_origin()
def edit_star():
    try:
        tmp = flask.request.json
        trueadmin = DbUser().get_one_by_name(tmp['username'])
        if trueadmin.rules != 'administrator':
            return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
        # None values
        if float(tmp['rectascensionh']) is None or float(tmp['rectascensionm']) is None or float(tmp['rectascensions']) is None:
            return jsonify({'result': False, 'message': "Rektascencja jest wymagana"})
        if float(tmp['declinationh']) is None or float(tmp['declinationm']) is None or float(tmp['declinations']) is None:
            return jsonify({'result': False, 'message': "Deklinacja jest wymagana"})
        # Limited values
        if float(tmp['rectascensionh']) == 24 and float(tmp['rectascensionm']) != 0 and float(tmp['rectascensions']) != 0:
            return jsonify({'result': False, 'message': "Rektascencja nie może przyjąć podanych wartości"})
        if float(tmp['declinationh']) == 90 and float(tmp['declinationm']) != 0 and float(tmp['declinations']) > 60:
            return jsonify({'result': False, 'message': "Deklinacja nie może przyjąć podanych wartości"})
        if float(tmp['rectascensionh']) > 24 or float(tmp['rectascensionm']) > 60 or float(tmp['rectascensions']) > 60:
            return jsonify({'result': False, 'message': "Rektascencja ma nieprawidłowe wartości"})
        if float(tmp['rectascensionh']) < 0 or float(tmp['rectascensionm']) < 0 or float(tmp['rectascensions']) < 0:
            return jsonify({'result': False, 'message': "Rektascencja ma nieprawidłowe wartości"})
        if float(tmp['declinationh']) > 90 or float(tmp['declinationm']) > 60 or float(tmp['declinations']) > 60:
            return jsonify({'result': False, 'message': "Deklinacja ma nieprawidłowe wartości"})
        if float(tmp['declinationh']) < -90 or float(tmp['declinationm']) < -60 or float(tmp['declinations']) < -60:
            return jsonify({'result': False, 'message': "Deklinacja ma nieprawidłowe wartości"})
        cons = DBConstellations().get_one_by_name(tmp['constellation'])
        tmp['constellation'] = cons.id
        if tmp['star_type'] is None:
            tmp['star_type'] = stars_type.StarsType['unknown']
        if tmp['radial_speed'] == '':
            tmp['radial_speed'] = None
        if tmp['distance'] == '':
            tmp['distance'] = None
        if tmp['brightness'] == '':
            tmp['brightness'] = None
        if tmp['mass'] == '':
            tmp['mass'] = None
        star = DBStars().update_entity(tmp, "edit")
        if star:
            return jsonify({'result': True, 'message': 'Dane gwiazdy zostały zmienione'})
        return jsonify({'result': False, 'message': 'Błąd edycji gwiazdy'})
    except AttributeError:
        return jsonify({'result': False, 'message': 'Błąd w parametrach gwiazdy'})


@field.route('/confirmed-star/<id>/<username>', methods=['GET'])
@cross_origin()
def confirmed_star(id, username):
    try:
        if request.method == 'GET':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            if DBStars().update_entity(id, "confirm"):
                ss = DBStars().get(id)
                idd = DbUser().get(ss.discaverer.id)
                ids = {'id': idd.id, 'star_number': int(idd.star_number) + 1}
                if DbUser().update_entity(ids, 'levelup'):
                    return jsonify({'result': True, 'message': 'Gwiazda została potwierdzona'})
            return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})

    except AttributeError:
        return jsonify({'result': False, 'message': 'Błąd potwierdzenia gwiazdy'})


@field.route('/form-list-admin-NO/<username>/<nrpage>', methods=['GET'])
@cross_origin()
def form_list_admin_NO(username, nrpage):
    try:
        if request.method == 'GET':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            query = DBStars().get_query().filter(Stars.confirmed == "NO").all()
            j = []
            for st in query:
                s = DBStars().get(st.id)
                if s is None:
                    return jsonify(j)
                if s.confirmed == "NO":
                    if s.discaverer is None:
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
                              'picture': str(s.constellation.picture),
                              })
                    if len(j) > 25:
                        break
            return jsonify(j)
    except TypeError:
        return jsonify({'result': False, 'message': "Błąd pobierania"})


@field.route('/form-list-admin-YES/<username>/<nrpage>', methods=['GET'])
@cross_origin()
def form_list_admin_YES(username, nrpage):
    try:
        if request.method == 'GET':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin.rules != 'administrator':
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            query = DBStars().get_query()
            if int(nrpage) <= 0:
                return jsonify({'result': False, 'message': "Numer strony nie może być ujemny"})
            items = query.limit(25).offset((int(nrpage) - 1) * 25).all()
            j = []
            for st in items:
                s = DBStars().get(st.id)
                if s is None:
                    return jsonify(j)
                if s.confirmed == "YES":
                    if s.discaverer is None:
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
                              'picture': str(s.constellation.picture),
                              })
            return jsonify(j)
        return jsonify({'result': False, 'message': "Błąd pobierania"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Błąd pobierania"})
    except IndexError:
        return jsonify({'result': False, 'message': "Nie istnieje w bazie więcej obiektów"})


@field.route('/add_new_star/<username>', methods=['POST'])
@cross_origin()
def add_new_star(username):
    try:
        if request.method == 'POST':
            trueadmin = DbUser().get_one_by_name(username)
            if trueadmin is None:
                return jsonify({'result': False, 'message': 'Nie posiadasz uprawnień'})
            tmp = flask.request.json
            star = Stars()
            cons = DBConstellations().get_one_by_name(tmp['constellation'])
            print(tmp)
            star.name = tmp['name']

            # None values
            if tmp['rectascensionh'] is None or tmp['rectascensionm'] is None or tmp['rectascensions'] is None:
                return jsonify({'result': False, 'message': "Rektascencja jest wymagana"})
            if tmp['declinationh'] is None or tmp['declinationm'] is None or tmp['declinations'] is None:
                return jsonify({'result': False, 'message': "Deklinacja jest wymagana"})

            # Integer integrity
            if not (val.integer_number(tmp['rectascensionh']) and val.integer_number(tmp['rectascensionm'])):
                return jsonify(
                    {'result': False, 'message': "Rektascencja może posiadać część ułamkową tylko dla sekund"})
            if not (val.integer_number(tmp['declinationh']) and val.integer_number(tmp['declinationm'])):
                return jsonify(
                    {'result': False, 'message': "Deklinacja może posiadać część ułamkową tylko dla sekund kątowytch"})

            # Compartment
            if tmp['rectascensionh'] == 24 and tmp['rectascensionm'] != 0 and tmp['rectascensions'] != 0:
                return jsonify({'result': False, 'message': "Rektascencja nie może przyjąć podanych wartości"})
            if tmp['declinationh'] == 90 and tmp['declinationm'] != 0 and tmp['declinations'] > 60:
                return jsonify({'result': False, 'message': "Deklinacja nie może przyjąć podanych wartości"})
            if tmp['rectascensionh'] > 24 or tmp['rectascensionm'] > 60 or tmp['rectascensions'] > 60:
                return jsonify({'result': False, 'message': "Rektascencja ma nieprawidłowe wartości"})
            if tmp['rectascensionh'] < 0 or tmp['rectascensionm'] < 0 or tmp['rectascensions'] < 0:
                return jsonify({'result': False, 'message': "Rektascencja ma nieprawidłowe wartości"})
            if tmp['declinationh'] > 90 or tmp['declinationm'] > 60 or tmp['declinations'] > 60:
                return jsonify({'result': False, 'message': "Deklinacja ma nieprawidłowe wartości"})
            if tmp['declinationh'] < -90 or tmp['declinationm'] < -60 or tmp['declinations'] < -60:
                return jsonify({'result': False, 'message': "Deklinacja ma nieprawidłowe wartości"})
            star.rectascensionh = tmp['rectascensionh']
            star.rectascensionm = tmp['rectascensionm']
            star.rectascensions = tmp['rectascensions']
            star.declinationh = tmp['declinationh']
            star.declinationm = tmp['declinationm']
            star.declinations = tmp['declinations']
            star.constelation_id = cons.id
            star.discaverer_id = tmp['discavererid']

            # Check number integrity
            if val.validationNone(tmp['radial_speed']):
                if not val.validate_text(tmp['radial_speed']):
                    raise Exceptions.Exceptions.ExceptionNotNumber
            if val.validationNone(tmp['distance']):
                if not val.validate_text(tmp['distance']):
                    raise Exceptions.Exceptions.ExceptionNotNumber
            if val.validationNone(tmp['brightness']):
                if not val.validate_text(tmp['brightness']):
                    raise Exceptions.Exceptions.ExceptionNotNumber
            if val.validationNone(tmp['mass']):
                if not val.validate_text(tmp['mass']):
                    raise Exceptions.Exceptions.ExceptionNotNumber

            # Check None value
            if tmp['star_type'] is None:
                tmp['star_type'] = stars_type.StarsType['unknown']
            star.star_type = tmp['star_type']
            if tmp['radial_speed'] == '':
                star.radial_speed = None
            else:
                star.radial_speed = float(tmp['radial_speed'])
            if tmp['distance'] == '':
                star.distance = None
            else:
                star.distance = float(tmp['distance'])
            if tmp['brightness'] == '':
                star.brightness = None
            else:
                star.brightness = float(tmp['brightness'])
            if tmp['mass'] == '':
                star.mass = None
            else:
                star.mass = float(tmp['mass'])
            star.greek_symbol = ''
            star.confirmed = "NO"
            DBStars(star).add_entity()
            return jsonify({'result': True, 'message': "Wysłano formularz"})
    except AttributeError:
        return jsonify({'result': False, 'message': "Podany gwiazdozbiór nie istnieje w bazie"})
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'result': False, 'message': "Podana nazwa gwiazdy istnieje w bazie. Proszę wybrać inną nazwę."})
    except Exceptions.Exceptions.ExceptionNotNumber:
        return jsonify({'result': False, 'message': "Paramtery gwiazdy muszą być cyframi"})


@field.route('/get_star_by_name/<star_name>', methods=['GET'])
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
                              'picture': str(s.constellation.picture),
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
                              'picture': str(s.constellation.picture),
                              })
            if len(j) >= 25:
                break
        return jsonify(j)
    except TypeError:
        return jsonify({'result': False, 'message': "Błąd nazwy gwiazdy"})


@field.route('/get_star_by_constellation/<constellation>', methods=['GET'])
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


@field.route('/get_one_star/<star_id>', methods=['GET'])
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
