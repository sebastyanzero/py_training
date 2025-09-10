# -*- coding: utf-8 -*-
from contacts import Contacts
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contacts(fname="fq1", mname="r2", lname="r3", nname="r4", title="r5", company="r6", address="r7",
                        home="t5", mobile="t6", work="t7", fax="t8", email1="u1", email2="u2", email3="u3",
                        sitehpage="u4", bday="1", bmonth="January", byear="2000", aday="7", amonth="May", ayear="2030"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contacts(fname="", mname="", lname="", nname="", title="", company="", address="",
                        home="", mobile="", work="", fax="", email1="", email2="", email3="",
                        sitehpage="", bday="", bmonth="", byear="", aday="", amonth="", ayear=""))
    app.logout()


