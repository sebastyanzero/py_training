from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        # self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")





    def create_contact(self, contacts):
        wd = self.wd
        # press add new contact
        wd.find_element_by_link_text("add new").click()
        # input  firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.fname)
        # input  middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.mname)
        # input  lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lname)
        # input  nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nname)
        # input
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        # input
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        # input
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)
        # input
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.home)
        # input
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        # input
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.work)
        # input
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contacts.fax)
        # input
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email1)
        # input
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        # input
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        # input
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contacts.sitehpage)
        # input  bd date
        ## input bday
        if contacts.bday != "":
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contacts.bday)
            #  wd.find_element_by_xpath("//option[@value='1']").click()
            # wd.find_element_by_xpath('//option[@value='+bday+']').click()
            # wd.find_element_by_xpath("//option[@value='" + bday + "']").click()
            wd.find_element_by_xpath("//select[@name='bday']//option[@value='" + contacts.bday + "']").click()
        ## input bmonth
        if contacts.bmonth != "":
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contacts.bmonth)
            # wd.find_element_by_xpath("//option[@value='January']").click() #rabotaet iznachalnaya stroka
            # wd.find_element_by_xpath("//option[@value='" + bmonth + "']").click()
            wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + contacts.bmonth + "']").click()
        ## input byear
        # if contacts.byear !="":
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contacts.byear)
        # input  ad date
        ## input aday
        if contacts.aday != "":
            wd.find_element_by_name("aday").click()
            # Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contacts.aday)
            # wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[3]").click() # iznachalnaya stroka
            # wd.find_element_by_css_selector("select[name=\"aday\"] &gt; option[value=\"1\"]").click()
            # wd.find_element_by_css_selector('select[name="aday"] &gt; option[value="'+aday+'"]').click()
            # wd.find_element_by_xpath("//option[@value='" + aday + "']").click()
            wd.find_element_by_xpath("//select[@name='aday']//option[@value='" + contacts.aday + "']").click()
        ## input amonth
        if contacts.amonth != "":
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contacts.amonth)
            # wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click() # iznachalnaya stroka
            # wd.find_element_by_xpath("//option[@value='" + amonth + "']").click()
            wd.find_element_by_xpath("//select[@name='amonth']//option[@value='" + contacts.amonth + "']").click()
        ## input ayear
        # if contacts.ayear != "":
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contacts.ayear)
        # press button Enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()