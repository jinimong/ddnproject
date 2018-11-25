from .common import *
from .secret import db_info
from os.path import basename, splitext

filename = splitext(basename(__file__))[0]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_info[filename]['NAME'],
        'USER': db_info[filename]['USER'],
        'PASSWORD': db_info[filename]['PASSWORD'],
        'HOST': db_info[filename]['HOST'],
        "PORT": db_info[filename]['PORT'],
    }
}
