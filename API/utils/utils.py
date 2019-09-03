ALLOWED_FILES = ['png','jpeg','jpg']



def allowed_file(filename):
  try :
    extension = filename.rsplit('.',1)[1]
    print(extension)
  except :
    return False
  return extension in ALLOWED_FILES


