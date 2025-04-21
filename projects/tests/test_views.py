# test_views.py
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_create_project(api_client, project_payload) -> None:
    # create a new project
    response_create = api_client.post('/api/project/', data=project_payload, format="json")
    logger.info(f"{response_create.data}")
    assert response_create.status_code == 201 
    assert response_create.data['data']['name'] == project_payload['name']

    # read the newly created project
    response_read = api_client.get('/api/project/', format="json")
    assert response_read.status_code == 200
    assert response_read.data['data'][0]['name'] == project_payload['name']