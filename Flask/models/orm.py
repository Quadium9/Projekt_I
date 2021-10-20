from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import common.stars_type as stars_type

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

    constelation_id = Column('constellation_id', Integer,
                             ForeignKey('constellations.id', ondelete="CASCADE"), nullable=False)
    discaverer_id = Column('discaverer_id', Integer,
                           ForeignKey('user.id', ondelete="CASCADE"))

    constellation = relationship('Constellations', lazy='subquery')
    discaverer = relationship('User', lazy='subquery')

    def __repr__(self):
        tmp = str(self.id) + ', ' + str(self.name) + ', ' + str(self.rectascension) + ', ' + str(self.declination) \
              + ', ' + str(self.constellation.name)

        # Radial speed is NULL
        if self.radial_speed is None:
            tmp = tmp + ', ' + str(stars_type.StarsType.unknown)
        else:
            tmp = tmp + ', ' + str(self.radial_speed)
        # Distance is NUll
        if self.distance is None:
            tmp = tmp + ', ' + str(stars_type.StarsType.unknown)
        else:
            tmp = tmp + ', ' + str(self.distance)
        # Brightness is NULL
        if self.brightness is None:
            tmp = tmp + ', ' + str(stars_type.StarsType.unknown)
        else:
            tmp = tmp + ', ' + str(self.brightness)
        # Star type is NULL
        if self.star_type is None:
            tmp = tmp + ', ' + str(stars_type.StarsType.unknown)
        else:
            tmp = tmp + ', ' + str(self.star_type)
        # Star mass is NULL
        if self.mass is None:
            tmp = tmp + ', ' + str(stars_type.StarsType.unknown)
        else:
            tmp = tmp + ', ' + str(self.mass)
        # Greek symbol is NULL
        if self.greek_symbol is None:
            tmp = tmp + ', None'
        else:
            tmp = tmp + ', ' + str(self.greek_symbol)
        # Discaverer is Null
        if self.discaverer.name is not None and self.discaverer.surname is not None:
            tmp = tmp + ', ' + self.discaverer.name + ', ' + self.discaverer.surname
        else:
            tmp = tmp + ', ' + str(stars_type.StarsType.unknown)
        return tmp


class Constellations(Base):
    __tablename__ = 'constellations'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    declination = Column('declination', String(100), nullable=False)
    symbolism = Column('symbolism', String(2000))
    sky_side = Column('sky_side', String(50))
    area = Column('area', Float)

    def __repr__(self):
        return str(self.id) + ', ' + str(self.name) + ', ' + str(self.declination) + ', ' + str(
            self.symbolism) + ', ' + str(self.sky_side) + \
               ', ' + str(float(self.area))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    id_star = Column('id_star', Integer, ForeignKey('stars.id', ondelete="CASCADE"), nullable=True)
    star = relationship('Stars', lazy='subquery')

    def __repr__(self):
        return str(self.id) + ", " + self.name + ', ' + str(self.star.name)


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
    star_name_out = Column("star_name_out", Integer, nullable=False)
    star_name_in = Column('star_name_in', Integer,
                          ForeignKey('stars.id', ondelete="CASCADE"), nullable=False)
    star = relationship('Stars', lazy='subquery')

    def __repr__(self):
        return str(self.id) + ', ' + str(self.star.id) + ', ' + str(self.star_name_out)
