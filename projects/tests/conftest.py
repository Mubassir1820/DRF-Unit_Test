import pytest
from datetime import date
from django.contrib.auth import get_user_model
from projects.models import Project
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser",password="testpassword")


@pytest.fixture
def project():
    return Project.objects.create(
        name='Test Project',
        description = 'Test project description',
        start_date = date(2024, 3, 1),
        end_date = date(2024, 4, 1),
    )


@pytest.fixture()
def api_client():
    yield APIClient()


@pytest.fixture
def project_payload(user):
    return {
        "name": "New project",
        "description": "Test project description",
        "start_date": "2024-01-01",
        "end_date": "2024-02-01",
        "team_members": [user.id]
    }