# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest

# scope="session" - означает, что фикстура запускается на всю сессию
@pytest.fixture(scope="session")
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture