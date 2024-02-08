import os, pass1

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{pass1.password()}@localhost/booksminiproject'
SQLALCHEMY_TRACK_MODIFICATIONS = False



