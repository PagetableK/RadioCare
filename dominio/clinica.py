from dataclasses import dataclass
from typing import Optional

@dataclass
class Departamento:
    nombre:str
    id_departamento: Optional[int] = None

@dataclass
class Municipio:
    nombre:str
    departamento:Departamento
    id_municipio: Optional[int] = None

@dataclass
class Sucursal:
    nombre:str 
    direccion:str
    municipio:Municipio
    id_sucursal: Optional[int] = None