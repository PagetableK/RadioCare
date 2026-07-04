from dataclasses import dataclass, field
from dominio.pacientes import Paciente
from dominio.personal import Radiologo
from dominio.clinica import  Sucursal
from typing import Optional
from datetime import datetime

@dataclass
class TipoExamen:
    nombre:str
    descripcion:str
    costo:float
    preindicaciones:str
    id_tipo_examen:Optional[int] = None

@dataclass
class OrganoExamen:
    nombre_organo:str
    longitud_organo:float
    ancho_organo:float
    volumen_organo:float
    id_organo_examen:Optional[int] = None
    
    def __post_init__(self):
        organos = ["Riñon izquierdo", "Riñon derecho", "Útero", "Hígado", "Próstata", "Vejiga", "Páncreas"]
        if self.nombre_organo.capitalize() not in organos:
            raise ValueError(f"Órgano inválido. \nÓrganos válidos:{organos}")
        

    def __eq__(self, other):
        if not isinstance(other, OrganoExamen):
            return False
        return self.id_organo_examen == other.id_organo_examen
    
@dataclass(frozen=True)
class ImagenExamen:
    url:str
    descripcion:str    

@dataclass
class Examen:
    fecha:datetime
    estado_examen:str
    tipo_examen:TipoExamen
    paciente:Paciente
    radiologo:Radiologo
    sucursal:Sucursal
    doctor_referencia:str = ""
    diagnostico:str = ""
    sugerencia:str = ""
    observaciones:str = ""
    organos:list[OrganoExamen] = field(default_factory=list)
    imagenes:list[ImagenExamen] = field(default_factory=list)
    id_examen:Optional[int] = None
    
    def __post_init__(self):
        estados = ["Pendiente", "Hecho", "Cancelado", "Reprogramado", "Seguimiento"]
        if self.estado_examen.capitalize() not in estados:
            raise ValueError(f"Estado de examen inválido. \nEstados de examen válidos:{estados}")
        if len(self.doctor_referencia) > 50:
            raise ValueError("El nombre del doctor de referencia no puede superar los 50 caracteres.")

    def __eq__(self, other):
        if not isinstance(other, Examen):
            return False
        return self.id_examen == other.id_examen