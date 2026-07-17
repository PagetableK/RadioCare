from flask import Blueprint, jsonify, request

pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route('/', methods=['GET'])
def get_pacientes():
    # Endpoint GET básico que retorna JSON
    pacientes = [
        {"id": 1, "nombre": "Juan Pérez", "edad": 45, "email": "juan.perez@example.com"},
        {"id": 2, "nombre": "María Gómez", "edad": 34, "email": "maria.gomez@example.com"}
    ]
    return jsonify(pacientes), 200

@pacientes_bp.route('/', methods=['POST'])
def create_paciente():
    # Endpoint POST básico que acepta JSON y retorna JSON
    data = request.get_json(silent=True) or {}
    
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es requerido"}), 400
        
    nuevo_paciente = {
        "id": 100,  # ID simulado
        "nombre": nombre,
        "edad": data.get('edad'),
        "email": data.get('email')
    }
    return jsonify({
        "mensaje": "Paciente creado exitosamente",
        "paciente": nuevo_paciente
    }), 201
