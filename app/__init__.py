import os
from flask import Flask

def create_app(script_info=None):
    app = Flask(__name__)

    from app.api.api import api
    app.register_blueprint(api)

    from app.views.views import views
    app.register_blueprint(views)

    @app.shell_context_processor
    def ctx():
        return {'app': app}
    return app