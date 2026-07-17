from flask import Blueprint, jsonify, request

radiologos_bp = Blueprint('radiologos', __name__)

@radiologos_bp.route('/', methods=['GET'])
def get_radiologos():
    # Endpoint GET básico que retorna JSON
    radiologos = [
        {"id": 1, "nombre": "Dr. Carlos Ruiz", "especialidad": "Neurorradiología", "licencia": "RAD-12345"},
        {"id": 2, "nombre": "Dra. Ana Martínez", "especialidad": "Radiología Pediátrica", "licencia": "RAD-67890"}
    ]
    return jsonify(radiologos), 200

@radiologos_bp.route('/', methods=['POST'])
def create_radiologo():
    # Endpoint POST básico que acepta JSON y retorna JSON
    data = request.get_json(silent=True) or {}
    
    nombre = data.get('nombre')
    especialidad = data.get('especialidad')
    if not nombre or not especialidad:
        return jsonify({"error": "Los campos 'nombre' y 'especialidad' son requeridos"}), 400
        
    nuevo_radiologo = {
        "id": 200,  # ID simulado
        "nombre": nombre,
        "especialidad": especialidad,
        "licencia": data.get('licencia', 'RAD-TEMP')
    }
    return jsonify({
        "mensaje": "Radiólogo creado exitosamente",
        "radiologo": nuevo_radiologo
    }), 201
