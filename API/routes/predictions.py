import logging
import os
import json 
from flask import request, jsonify, Response, Blueprint
from werkzeug.utils import secure_filename

from . import model

from ..utils.utils import allowed_file




prediction_api = Blueprint('prediction_api',__name__)

@prediction_api.route('/',methods=['GET','POST'])
def make_prediction():
  if request.method == 'GET':
    return 'route not Gettable'

 
  try :
    logging.info("request file",request.files)
    print("request file",request.files)
    file = request.files.get('file',None)
  except Exception as error:
    return jsonify({"success":False, "error":error}), 400

  if file == None :
      return jsonify({"success":False, "error":"no correct link", "data": request.files}), 400

  if file.filename == '':
    return jsonify({"success":False, "error":"no file present"}), 400
  
  if allowed_file(file.filename) == False:
    return jsonify({"success":False, "error":"only png, jpg and jpeg are allowed"}), 400
  
  filename = secure_filename(file.filename)
  
  image_path = f'{os.getcwd()}/API/tmp/{filename}'
  file.save(image_path)

  try :
    result = model.classify_images(image_path)
    response = jsonify({"success":True, "data":result})
    #os.remove(image_path)
    return response
    os.remove(image_path)
  except Exception as error:
    os.remove(image_path)
    return jsonify({"success":False, "error":error}), 400

