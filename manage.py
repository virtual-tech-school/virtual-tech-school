from flask.cli import FlaskGroup
from app import create_app
from flask import current_app

app = create_app()
cli = FlaskGroup(create_app=create_app) #For adding CLI commands to the application later

if __name__ == '__main__':
    cli()