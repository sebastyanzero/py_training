# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

""" комментарий """ #@pytest.fixture(scope="session")
@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="p1", header="p2", footer="p3"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

