import pytest
from users.tests.climber_factory import ClimberFactory
from graphene.test import Client as GrapheneClient
from schema import schema


@pytest.fixture
def climber():
    return ClimberFactory

@pytest.fixture
def graph_client():
    return GrapheneClient(schema)
