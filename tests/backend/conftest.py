from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import app as app_module


@pytest.fixture
def client():
    initial_activities = deepcopy(app_module.activities)

    with TestClient(app_module.app) as test_client:
        yield test_client

    app_module.activities.clear()
    app_module.activities.update(initial_activities)