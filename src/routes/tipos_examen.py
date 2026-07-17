from flask import Blueprint, jsonify, request

tipos_examen_bp = Blueprint('tipos_examen', __name__)

@tipos_examen_bp.route('/', methods=['GET'])
def get_tipos_examen():
    # Endpoint GET básico que retorna JSON
    tipos_examen = [
        {"id": 1, "nombre": "Radiografía de Tórax", "descripcion": "Estudio radiológico de los pulmones y corazón"},
        {"id": 2, "nombre": "Resonancia Magnética Cerebral", "descripcion": "Estudio detallado del cerebro utilizando campos magnéticos"}
    ]
    return jsonify(tipos_examen), 200

@tipos_examen_bp.route('/', methods=['POST'])
def create_tipo_examen():
    # Endpoint POST básico que acepta JSON y retorna JSON
    data = request.get_json(silent=True) or {}
    
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es requerido"}), 400
        
    nuevo_tipo_examen = {
        "id": 400,  # ID simulado
        "nombre": nombre,
        "descripcion": data.get('descripcion', '')
    }
    return jsonify({
        "mensaje": "Tipo de examen creado exitosamente",
        "tipo_examen": nuevo_tipo_examen
    }), 201
