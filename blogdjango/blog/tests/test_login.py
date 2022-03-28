from django.urls.base import reverse
import pytest

@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('login'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200

