from sqlalchemy.orm import Session
from model import Libro
from schemas import Librosquemas

def get_libro(db:Session,skip:int=0,limit:int=100):
    return db.query(Libro).offset(skip).limit(limit).all()

def get_libro_id(db:Session,libro_id:int):
    return db.query(Libro).filter(Libro.id == libro_id).first()

def crear_libro(db:Session, libro:Librosquemas):
    _libro = Libro(id=libro.id,titulo=libro.titulo,descripcion=libro.descripcion)
    db.add(_libro)
    db.commit()
    db.refresh(_libro)
    return _libro

def eliminar_libro(db:Session,libro_id:int):
    _libro = get_libro_id(db=db,libro_id=libro_id)
    db.delete(_libro)
    db.commit()

def actualiza_libro(db:Session,libro_id:int,titulo:str,descripcion:str):
    _libro = get_libro_id(db=db,libro_id=libro_id)
    _libro.titulo = titulo
    _libro.descripcion = descripcion
    db.commit()
    db.refresh(_libro)
    return _libro