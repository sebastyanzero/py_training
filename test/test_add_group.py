# -*- coding: utf-8 -*-
from model.group import Group

""" комментарий """

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="p1", header="p2", footer="p3"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

