
from django.urls.base import reverse
import pytest
from blogdjango.django_assertions import assert_contains

@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Blog Django </title>')


def test_link(resp):
    assert_contains(resp, f'href="{reverse("home")}">Blog Django </a>')