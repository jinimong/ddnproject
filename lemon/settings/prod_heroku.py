from .common import *
from .secret import db_info

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_info['NAME'],
        'USER': db_info['USER'],
        'PASSWORD': db_info['PASSWORD'],
        'HOST': db_info['HOST'],
        "PORT": db_info['PORT'],
    }
}
