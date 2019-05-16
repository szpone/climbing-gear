import pytest
from django.contrib.auth import get_user_model

Climber = get_user_model()


@pytest.mark.django_db
def test_get_climber(graph_client, climber):
    query = (
        (
            """
            query {
                climber(id: %s) {
                    id
                }
            }
        """
        )
        % climber.id
    )

    executed = graph_client.execute(query)

    assert executed["data"]["climber"]["id"] == str(climber.id)


@pytest.mark.django_db
def test_get_climbers(graph_client):
    query = """
            query {
                climbers {
                    id
                    }
                }
        """

    executed = graph_client.execute(query)

    assert len(executed["data"]["climbers"]) == Climber.objects.all().count()


@pytest.mark.django_db
def test_get_none_climber(graph_client):
    query = """
            query {
                climber(id: 99999) {
                    id
                }
            }
        """

    executed = graph_client.execute(query)

    assert executed["data"]["climber"] is None
