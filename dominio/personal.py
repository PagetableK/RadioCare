from dataclasses import dataclass
from typing import Optional
import re

@dataclass
class Radiologo:
    nombre:str 
    apellido:str
    telefono:int
    correo:str
    id_radiologo:Optional[int] = None

    def __pos_init__(self):
        if len(self.nombre) > 40:
            raise ValueError("El nombre no puede tener más de 40 caracteres")
        if len(self.apellido) > 40:
            raise ValueError("El apellido no puede tener más de 40 caracteres")
        self.telefono = self.telefono.strip()
        patron_telefono = re.compile(r'^\d{4}-\d{4}$')
        if not patron_telefono.match(self.telefono):
            raise ValueError("El teléfono debe tener el formato XXXX-XXXX")
        if len(self.correo) > 25 or "@" not in self.correo or "." not in self.correo:
            raise ValueError("El formato del correo no es valido.")


    def __eq__(self, other):
        if not isinstance(other, Radiologo):
            return False
        return self.id_radiologo == other.id_radiologo
    