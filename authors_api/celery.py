import os 

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

app = Celery("authors_api")

app.config_from_object('django.conf:settings', namespace='CELERY')

# we add a lamda finction as we changed the default name of the apps we add to the project
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)