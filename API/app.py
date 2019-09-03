import logging
import keras
from flask import Flask, request, jsonify
from .routes.predictions import prediction_api
from .config import app_config

#------- Basic setup -------
# remove keras cach and initialize logger
logging.basicConfig(format='%(asctime)s %(message)s')


def create_app ():
  app = Flask(__name__)
  app.config.from_object(app_config['development'])
  app.register_blueprint(prediction_api, url_prefix='/bot')
  @app.route('/ping',methods=['GET'])
  def is_server_running():
    return 'server running'

  return app