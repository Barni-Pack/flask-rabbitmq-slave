from flask import Flask

app = Flask(__name__)

app.config.from_object('app.configuration.Config')

from app import views