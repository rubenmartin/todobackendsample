from base import *
import os

# Databese
# https://docs.djangorproject.com/en/1.8/ref/seetings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
		'USER': os.environ.get('MYSQL_USER', 'todo'),
		'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'password'),
		'HOST': os.environ.get('MYSQL_HOST','localhost'),
		'PORT': os.environ.get('MYSQL_PORT',3306)
	}
}