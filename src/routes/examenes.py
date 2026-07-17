from flask import Blueprint, jsonify, request

examenes_bp = Blueprint('examenes', __name__)

@examenes_bp.route('/', methods=['GET'])
def get_examenes():
    # Endpoint GET básico que retorna JSON
    examenes = [
        {"id": 1, "paciente_id": 1, "radiologo_id": 1, "tipo_examen_id": 2, "fecha": "2026-07-14", "estado": "Completado"},
        {"id": 2, "paciente_id": 2, "radiologo_id": 2, "tipo_examen_id": 1, "fecha": "2026-07-15", "estado": "Pendiente"}
    ]
    return jsonify(examenes), 200

@examenes_bp.route('/', methods=['POST'])
def create_examen():
    # Endpoint POST básico que acepta JSON y retorna JSON
    data = request.get_json(silent=True) or {}
    
    paciente_id = data.get('paciente_id')
    radiologo_id = data.get('radiologo_id')
    tipo_examen_id = data.get('tipo_examen_id')
    
    if not paciente_id or not radiologo_id or not tipo_examen_id:
        return jsonify({"error": "Los campos 'paciente_id', 'radiologo_id' y 'tipo_examen_id' son requeridos"}), 400
        
    nuevo_examen = {
        "id": 300,  # ID simulado
        "paciente_id": paciente_id,
        "radiologo_id": radiologo_id,
        "tipo_examen_id": tipo_examen_id,
        "fecha": data.get('fecha', '2026-07-14'),
        "estado": data.get('estado', 'Pendiente')
    }
    return jsonify({
        "mensaje": "Examen creado exitosamente",
        "examen": nuevo_examen
    }), 201
