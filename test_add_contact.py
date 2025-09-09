# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re
from contacts import Contacts
from application import Application
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

    """

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()



    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main() """
