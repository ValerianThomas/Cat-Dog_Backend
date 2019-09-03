import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
   

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False

app_config = {
    'development': Development,
    'production': Production,
}