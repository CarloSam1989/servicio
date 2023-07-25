from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field


T=TypeVar('T')

class Librosquemas(BaseModel):
    id: Optional[int]=None
    titulo:Optional[str]=None
    descripcion:Optional[str]=None

    class Config:
        orm_mode=True

class RespuestaLibro(BaseModel):
    parametro: Librosquemas = Field(...)

class Respuesta (BaseModel, Generic[T]):
    code: int
    status: str
    mensaje:str
    resultado: Optional[T]
    
    
