import pytest
from datetime import date
from django.contrib.auth import get_user_model
from projects.models import Project

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