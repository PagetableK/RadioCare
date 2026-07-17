from flask import Blueprint, jsonify, request

organos_bp = Blueprint('organos', __name__)

@organos_bp.route('/', methods=['GET'])
def get_organos():
    # Endpoint GET básico que retorna JSON
    organos = [
        {"id": 1, "nombre": "Cerebro", "sistema": "Sistema Nervioso Central"},
        {"id": 2, "nombre": "Corazón", "sistema": "Sistema Cardiovascular"},
        {"id": 3, "nombre": "Pulmones", "sistema": "Sistema Respiratorio"}
    ]
    return jsonify(organos), 200

@organos_bp.route('/', methods=['POST'])
def create_organo():
    # Endpoint POST básico que acepta JSON y retorna JSON
    data = request.get_json(silent=True) or {}
    
    nombre = data.get('nombre')
    sistema = data.get('sistema')
    if not nombre or not sistema:
        return jsonify({"error": "Los campos 'nombre' y 'sistema' son requeridos"}), 400
        
    nuevo_organo = {
        "id": 500,  # ID simulado
        "nombre": nombre,
        "sistema": sistema
    }
    return jsonify({
        "mensaje": "Órgano creado exitosamente",
        "organo": nuevo_organo
    }), 201
