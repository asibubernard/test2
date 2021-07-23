from .base import *
import dj_tatabase_url

env = os.environ.copy()


SECRET_KEY = os.environ.get('SECRET_KEY',)

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','localhost', '.herokuapp.com']

#whitenoise 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # new

DATABASE_URL = os.environ.get("DATABASE_URL")
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES["default"].update(db_from_env)