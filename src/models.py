import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    mail = Column(String(250), ForeignKey('usuario.nickname'), nullable=False, )
    personajefavorito=Column(String(250))
    planetafavorito = Column(String(250))
    vehiculofavorito= Column(Integer,)
    relacionPersonajes = relationship("Personajes")
    relacionPlaneta = relationship("Planeta")
    relacionVehiculos = relationship("Vehiculo")

class Personajes(Base):
    __tablename__ = 'personajes'
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favoritos.personajefavorito'), nullable=False, )
    gender =Column(String(250))
    homeworld = Column(String(250))


class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favoritos.planetafavorito'), nullable=False, )
    population = Column(Integer)
    homeworld = Column(String(250))

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    name = Column(String(250),  ForeignKey('favoritos.vehiculofavorito'), primary_key=True)
    modelo = Column(String(250), nullable=False, )
    manufactura= Column(String(250))
    
class Usuario(Base):
    __tablename__ = 'usuario'
    nickname = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mail= Column(String(50))
    relacionFavoritos = relationship("Favoritos")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')