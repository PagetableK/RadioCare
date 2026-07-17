from flask import Flask

def create_app(test_config=None):
    """
    Patrón para inicializar la app de Flask.
    """
    app = Flask(__name__)
    
    # Default configuration
    app.config.from_mapping(
        SECRET_KEY='dev_secret_key',
    )
    
    if test_config is not None:
        app.config.from_mapping(test_config)

    # Register Blueprints
    from .routes.pacientes import pacientes_bp
    from .routes.radiologos import radiologos_bp
    from .routes.examenes import examenes_bp
    from .routes.tipos_examen import tipos_examen_bp
    from .routes.organos import organos_bp

    app.register_blueprint(pacientes_bp, url_prefix='/api/pacientes')
    app.register_blueprint(radiologos_bp, url_prefix='/api/radiologos')
    app.register_blueprint(examenes_bp, url_prefix='/api/examenes')
    app.register_blueprint(tipos_examen_bp, url_prefix='/api/tipos-examen')
    app.register_blueprint(organos_bp, url_prefix='/api/organos')

    # Root route for API information
    @app.route('/')
    def index():
        return {
            "nombre": "RadioCare API",
            "version": "1.0.0",
            "estado": "online",
            "endpoints": {
                "pacientes": "/api/pacientes/",
                "radiologos": "/api/radiologos/",
                "examenes": "/api/examenes/",
                "tipos_examen": "/api/tipos-examen/",
                "organos": "/api/organos/"
            }
        }, 200

    return app
