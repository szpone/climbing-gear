import pytest


@pytest.mark.django_db
def test_get_climber(graph_client, climber):
    query = (
        """
            query {
                climber(id: %s) {
                    id
                }
            }
        """
    )

    executed = graph_client(query)

    assert executed["data"]["climber"]["id"] == str(climber.id)
