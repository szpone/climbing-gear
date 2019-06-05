from .base import *
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="ri2*eg#6!85j)v%k$t%ps=q@%wb-p#twj3xijiji8&h$)$)5j*"
)

TEST_RUNNER = "django.test.runner.DiscoverRunner"
