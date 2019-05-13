import factory
from factory import DjangoModelFactory
from faker import Faker
from climbing_gear.settings import base

faker = Faker()


class ClimberFactory(DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = base.AUTH_USER_MODEL
        django_get_or_create = ["username"]
