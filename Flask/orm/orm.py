from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Stars(Base):
    __tablename__ = 'stars'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(255), nullable=False)
    rectascension = Column('rectascension', String(255))
    declination = Column('declination', String(255))
    radial_speed = Column('radial_speed', DECIMAL(60, 8))
    distance = Column('distance', DECIMAL(60, 8), nullable=False)
    brightness = Column('brightness', DECIMAL(60, 8), nullable=False)
    spectral_type = Column('spectral_type', String(255))
    mass = Column('mass', DECIMAL(60, 8), nullable=True)
    starmain = Column('star_main', Integer, nullable=False)
    type = Column('type', String(255))
    metallicity = Column('metallicity', DECIMAL(60, 8))
    age = Column('age', DECIMAL(60, 8))
    link = Column('link', String(255))
    constelation_id = Column('constelation_id', Integer,
                             ForeignKey('constelations.id', ondelete="CASCADE"), nullable=False)
    constelation = relationship('Constellations', lazy='subquery')

    def __repr__(self):
        obj = self.name + ', ' + self.rectascension + ', ' + self.declination + ', ' + str(
            float(self.radial_speed)) + ', ' + str(float(self.distance)) + ', ' + str(
            float(self.brightness)) + ', ' + self.spectral_type + ', ' + str(
            self.starmain) + ', ' + self.constelation.name + ', ' + self.type + ', ' + str(
            float(self.metallicity)) + ', ' + str(float(self.age))

        if (self.mass is not None):
            obj = obj + ", " + str(float(self.mass))

        if (self.link is not None):
            obj = obj + ', ' + self.link

        return obj


class Constellations(Base):
    __tablename__ = 'constelations'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(255), nullable=False)
    declination = Column('declination', DECIMAL(65, 7), nullable=False)
    mainstar = Column('mainStars', Integer, nullable=False)
    symbolism = Column('symbolism', String(1000))
    sky_side = Column('sky_side', Integer)
    brightest_star = Column('brightest_star', String(255))
    area = Column('area', DECIMAL(60, 8))

    def __repr__(self):
        return self.name + ', ' + self.declination + ', ' + str(
            self.mainstar) + ', ' + self.symbolism + ', ' + str(
            self.sky_side) + ', ' + self.brightest_star + ', ' + str(float(self.area))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(255), nullable=False)
    id_star = Column('id_star', Integer, ForeignKey('stars.id', ondelete="CASCADE"), nullable=True)
    star = relationship('Stars', lazy='subquery')

    def __repr__(self):
        return self.name + ', ' + self.star.name

