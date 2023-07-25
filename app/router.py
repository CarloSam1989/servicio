from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Librosquemas, RespuestaLibro, Respuesta
import crud

router = APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/crear')
async def crear(request:RespuestaLibro,db:Session=Depends(get_db)):
    crud.crear_libro(db, libro = request.parametro)
    return Respuesta(code=200,status="Ok",mensaje="Libro creado").dict(exclude_none=True)

@router.get("/")
async def get(db:Session = Depends(get_db)):
    _libro = crud.get_libro(db, 0, 100)
    return Respuesta(code=200, status="Ok",mensaje="Todos los libros",resultado=_libro).dict(exclude_none=True)

@router.get("/{id}")
async def get_id(id:int, db:Session = Depends(get_db)):
    _libro = crud.get_libro_id(db,id)
    return Respuesta(code=200, status="Ok", mensaje="El libro es", resultado=_libro).dict(exclude_none=True)

@router.post("/actualizar")
async def actualizar_libro(request: RespuestaLibro, db:Session = Depends(get_db)):
    _libro=crud.actualiza_libro(db,libro_id=request.parametro.id,titulo=request.parametro.titulo,descripcion=request.parametro.descripcion)
    return Respuesta(code=200, status="Ok", mensaje="El libro se actualizo", resultado=_libro)

@router.delete("/{id}")
async def eliminar(id:int, db:Session=Depends(get_db)):
    crud.eliminar_libro(db, libro_id=id)
    return Respuesta(code=200, status="Ok", mensaje="El libro se elimino").dict(exclude_none=True)