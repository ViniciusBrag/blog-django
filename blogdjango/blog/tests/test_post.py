
from django.urls.base import reverse
import pytest

@pytest.fixture
def resp(client):
    resp = client.get(reverse('blog:home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200