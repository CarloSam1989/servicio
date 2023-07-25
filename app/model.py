from sqlalchemy import Column, Integer, String
from config import Base

class Libro(Base):
    __tablename__='libro'

    id=Column(Integer, primary_key=True)
    titulo=Column(String)
    descripcion=Column(String)