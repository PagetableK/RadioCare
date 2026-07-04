from dataclasses import dataclass
from typing import Optional
import re

@dataclass
class Paciente:
    nombre:str 
    apellido:str
    edad:int
    telefono:str
    id_paciente: Optional[int] = None

    def __post_init__(self):
        if len(self.nombre) > 40:
            raise ValueError("El nombre no puede tener más de 40 caracteres")
        if len(self.apellido) > 40:
            raise ValueError("El apellido no puede tener más de 40 caracteres")
        self.telefono = self.telefono.strip()
        patron_telefono = re.compile(r'^\d{4}-\d{4}$')
        if not patron_telefono.match(self.telefono):
            raise ValueError("El teléfono debe tener el formato XXXX-XXXX")

    
    def __eq__(self, other):
        if not isinstance(other, Paciente):
            return False
        return self.id_paciente == other.id_paciente
