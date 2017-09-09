from django.conf import settings

from pyhunter import PyHunter

hunter = PyHunter(settings.HUNTER_API_KEY)
