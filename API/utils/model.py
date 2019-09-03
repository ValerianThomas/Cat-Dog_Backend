import os
import logging
import numpy as np
from keras.models import load_model
from keras.preprocessing import image 
from keras import backend as K 

MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/128_128.h5'


class Model:
  instance = None
  @classmethod
  def get_model(cls):
    if not cls.instance:
      return Model()

  def __init__(self):
    self.model = load_model(MODEL_PATH)
  
  def classify_images(self,img):
    print('image path', img)
    test_image = image.load_img(img,target_size=(128,128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    try:
      results = self.model.predict(test_image)
      print('raw',results)
      result_map = map(lambda result:{"cat":int(result[0]*100),"dog":int(result[1]*100)},results)
      result_map = list(result_map)
      return result_map
    except Exception as error:
      return error
    

if __name__ == '__main__':
  image_name = 'neyti3.png'
  image_path = f'/Users/valerian/Documents/IT/Learning/Data Science/DeepLearning/Cat_Dog/API/tmp/{image_name}'
  model = Model.get_model()
  result = model.classify_images(image_path)
  print("clean",result)
