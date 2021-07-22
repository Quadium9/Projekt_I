from models.orm import *
from database.db_drawingconstellation import DbDrawingConstellation
from database.db_planet import DBPlanet
from database.db_stars import DBStars
from database.db_user import DbUser
from database.db_constelations import DBConstellations


cons = Constellations()
cons.name = 'constellationsname'
cons.declination = 'constellationdeclination'
cons.symbolism = 'constellationsymbolism'
cons.sky_side = 'sky_side'
cons.area = 1.2

user = User()
user.name = 'admin'
user.surname = 'admin'
user.login = 'admin'
user.password = 'admin'
user.email = 'admin'

draw = DrawingConstellation()
draw.connected_Star = 1

stars = Stars()
stars.name = 'test'
stars.rectascension = 'sdfsd'
stars.declination = 'fdfs'
stars.radial_speed = 'dfdsfsdfdsf'
stars.distance = 'sdfdfds'
stars.brightness = 'sdafdsfsdf'
stars.star_type = 'dwarf'
stars.mass = 'big mass'
stars.greek_symbol = 'a'
stars.constelation_id = 1
stars.discaverer_id = 1
stars.drawing_star = 1
stars.constellation = cons
stars.drawing = draw
stars.discaverer = user

planet = Planet()
planet.name = 'planet'
planet.id_star = 1

dbCons = DBConstellations(cons)
dbCons.add_entity()

users = DbUser(user)
users.add_entity()

drawings = DbDrawingConstellation(draw)
drawings.add_entity()

dbStars = DBStars(stars)
dbStars.add_entity()

dbPlan = DBPlanet(planet)
dbPlan.add_entity()
