from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Stars(Base):
    __tablename__ = 'stars'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    rectascension = Column('rectascension', String(20), nullable=False)
    declination = Column('declination', String(20), nullable=False)
    radial_speed = Column('radial_speed', String(20))
    distance = Column('distance', String(20))
    brightness = Column('brightness', String(20))
    star_type = Column('star_type', String(50))
    mass = Column('mass', String(20))
    greek_symbol = Column('greek_symbols', String(1))

    drawing_star = Column('drawing_star', Integer,
                          ForeignKey('drawing_constellation.id', ondelete="CASCADE"))
    constelation_id = Column('constellation_id', Integer,
                             ForeignKey('constellations.id', ondelete="CASCADE"), nullable=False)
    discaverer_id = Column('discaverer_id', Integer,
                           ForeignKey('user.id', ondelete="CASCADE"))

    constellation = relationship('Constellations', lazy='subquery')
    drawing = relationship('DrawingConstellation', lazy='subquery')
    discaverer = relationship('User', lazy='subquery')

    def __repr__(self):
        return str(self.id) + ', ' + str(self.name) + ', ' + str(self.rectascension) + ', ' + str(self.declination)\
               + ', ' + str(self.radial_speed) + ', ' + str(self.distance) + ', ' + str(self.brightness) + ', ' + str(self.star_type) + ', ' + str(self.mass) + ', ' + \
                    str(self.greek_symbol) + ', ' + str(self.drawing_star) + ', ' + str(self.constellation.name) + ', '\
                        + str(self.discaverer.name) + ', ' + str(self.discaverer.surname)


class Constellations(Base):
    __tablename__ = 'constellations'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    declination = Column('declination', String(100), nullable=False)
    symbolism = Column('symbolism', String(2000))
    sky_side = Column('sky_side', String(50))
    area = Column('area', Float)

    def __repr__(self):
        return self.id + ', ' + self.name + ', ' + self.declination + ', ' + self.symbolism + ', ' + self.sky_side + \
               ', ' + str(float(self.area))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    id_star = Column('id_star', Integer, ForeignKey('stars.id', ondelete="CASCADE"), nullable=True)
    star = relationship('Stars', lazy='subquery')

    def __repr__(self):
        return self.id + ", " + self.name + ', ' + self.star.name


class User(Base):
    __tablename__ = "user"
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    surname = Column('surname', String(100), nullable=False)
    login = Column('login', String(100), nullable=False)
    password = Column('password', String(100), nullable=False)
    email = Column('email', String(100), nullable=False)

    def __repr__(self):
        return str(self.id) + ', ' + self.name + ', ' + self.surname + ', ' + self.login + ', ' + self.password + ', ' \
                + self.email


class DrawingConstellation(Base):
    __tablename__ = "drawing_constellation"
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    connected_Star = Column("connected_star", Integer)

    def __repr__(self):
        return str(self.connected_Star)



