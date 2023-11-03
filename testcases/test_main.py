import time
import pytest

from testcases.test_contact import Contact
from testcases.test_base import BaseTest
from testcases.test_login_page import TestLogin
from utils import read_data


@pytest.mark.usefixtures
class Testherokuapp(BaseTest):

    @pytest.fixture
    def class_objects(self):
        self.lp = TestLogin(self.driver)
        self.cd = Contact(self.driver)

    @pytest.mark.usefixtures
    def test_login(self, class_objects):
        self.lp.test_home_page()
        self.lp.test_login_page()

    def test_contact_details(self, class_objects):
        # self.lp.test_home_page()
        # self.lp.test_login_page()
        self.cd.add_contact_page1()
        self.cd.add_contact_page2()
        self.cd.add_contact_page3()
        self.cd.add_contact_page4()
        self.cd.add_contact_page5()
        self.cd.add_contact_page6()
        self.cd.add_contact_page7()
        # self.cd.add_contact_page8()
        # self.cd.add_contact_page9()
        # self.cd.add_contact_page10()
        # self.cd.add_contact_page11()
        # self.cd.add_contact_page12()
        # self.cd.add_contact_page13()
        # self.cd.add_contact_page14()
        # self.cd.add_contact_page15()
        # self.cd.add_contact_page16()
        # self.cd.add_contact_page17()
        # self.cd.add_contact_page18()
        # self.cd.add_contact_page19()
        # self.cd.add_contact_page20()
        # self.cd.add_contact_page21()
        # self.cd.add_contact_page22()
        # self.cd.add_contact_page23()
        # self.cd.add_contact_page24()
        # self.cd.add_contact_page25()
        # self.cd.add_contact_page26()
        # self.cd.add_contact_page27()
        # self.cd.add_contact_page28()
        # self.cd.add_contact_page29()
        # self.cd.add_contact_page30()
        # self.cd.add_contact_page31()
        # self.cd.add_contact_page34()
        # self.cd.add_contact_page35()
        # self.cd.add_contact_page36()
        #
        # self.cd.add_contact_page38()
        # self.cd.add_contact_page39()
        # self.cd.add_contact_page40()
        # self.cd.add_contact_page41()
        # self.cd.add_contact_page42()
        # self.cd.add_contact_page43()
        # self.cd.add_contact_page44()
        # self.cd.add_contact_page45()
        # self.cd.add_contact_page46()
        # self.cd.add_contact_page47()
        # self.cd.add_contact_page49()
        # self.cd.add_contact_page50()
        # self.cd.add_contact_page51()
        # self.cd.add_contact_page52()

    # def test_contact(self, class_objects):
    #     # self.lp.test_home_page()
    #     # self.lp.test_login_page()
    #     self.cd.test_validate_contact_details()

    def test_delete(self, class_objects):
        self.cd.test_delete()

    def test_delete_all_contacts(self, class_objects):
        self.lp.test_home_page()
        self.lp.test_login_page()

        self.cd.test_delete()
