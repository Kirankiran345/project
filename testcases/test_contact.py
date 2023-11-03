import time

import pytest

from pages.addcontact import Contacts
from pages.basepage import BasePage
from utils import read_data
import logging


class Contact(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.c = Contacts(driver)

    def add_contact_page(self, data_key):
        data = read_data()[data_key]
        self.c.add_newcontact()
        self.c.first_name(data["fname"])
        self.c.last_name(data["lname"])
        self.c.date_of_birth(data["dob"])
        self.c.email(data["email"])
        self.c.phone_number(data["phone_number"])
        self.c.Street_Address1(data["adress1"])
        self.c.Street_Address2(data["adress2"])
        self.c.city(data["city"])
        self.c.state(data["state"])
        self.c.postal_code(data["post_code"])
        self.c.country(data["country"])
        self.c.click_submit()
        time.sleep(3)

    def add_contact_page1(self):
        self.add_contact_page("data1")

    def add_contact_page2(self):
        self.add_contact_page("data2")

    def add_contact_page3(self):
        self.add_contact_page("data3")

    def add_contact_page4(self):
        self.add_contact_page("data4")

    def add_contact_page5(self):
        self.add_contact_page("data5")

    def add_contact_page6(self):
        self.add_contact_page("data6")

    def add_contact_page7(self):
        self.add_contact_page("data7")

    def add_contact_page8(self):
        self.add_contact_page("data8")

    def add_contact_page9(self):
        self.add_contact_page("data9")

    def add_contact_page10(self):
        self.add_contact_page("data10")

    def add_contact_page11(self):
        self.add_contact_page("data11")

    def add_contact_page12(self):
        self.add_contact_page("data12")

    def add_contact_page13(self):
        self.add_contact_page("data13")

    def add_contact_page14(self):
        self.add_contact_page("data14")

    def add_contact_page15(self):
        self.add_contact_page("data15")

    def add_contact_page16(self):
        self.add_contact_page("data16")

    def add_contact_page17(self):
        self.add_contact_page("data17")

    def add_contact_page18(self):
        self.add_contact_page("data18")

    def add_contact_page19(self):
        self.add_contact_page("data19")

    def add_contact_page20(self):
        self.add_contact_page("data20")

    def add_contact_page21(self):
        self.add_contact_page("data21")

    def add_contact_page22(self):
        self.add_contact_page("data22")

    def add_contact_page23(self):
        self.add_contact_page("data23")

    def add_contact_page24(self):
        self.add_contact_page("data24")

    def add_contact_page25(self):
        self.add_contact_page("data25")

    def add_contact_page26(self):
        self.add_contact_page("data26")

    def add_contact_page27(self):
        self.add_contact_page("data27")

    def add_contact_page28(self):
        self.add_contact_page("data28")

    def add_contact_page29(self):
        self.add_contact_page("data29")

    def add_contact_page30(self):
        self.add_contact_page("data30")

    def add_contact_page31(self):
        self.add_contact_page("data31")

    # def add_contact_page32(self):
    #     self.add_contact_page("data32")
    #
    # def add_contact_page33(self):
    #     self.add_contact_page("data33")

    def add_contact_page34(self):
        self.add_contact_page("data34")

    def add_contact_page35(self):
        self.add_contact_page("data35")

    def add_contact_page36(self):
        self.add_contact_page("data36")

    def add_contact_page37(self):
        self.add_contact_page("data37")

    def add_contact_page38(self):
        self.add_contact_page("data38")

    def add_contact_page39(self):
        self.add_contact_page("data39")

    def add_contact_page40(self):
        self.add_contact_page("data40")

    def add_contact_page41(self):
        self.add_contact_page("data41")

    def add_contact_page42(self):
        self.add_contact_page("data42")

    def add_contact_page43(self):
        self.add_contact_page("data43")

    def add_contact_page44(self):
        self.add_contact_page("data44")

    def add_contact_page45(self):
        self.add_contact_page("data45")

    def add_contact_page46(self):
        self.add_contact_page("data46")

    def add_contact_page47(self):
        self.add_contact_page("data47")

    def add_contact_page48(self):
        self.add_contact_page("data48")

    def add_contact_page49(self):
        self.add_contact_page("data49")

    def add_contact_page50(self):
        self.add_contact_page("data50")

    def add_contact_page51(self):
        self.add_contact_page("data51")

    def add_contact_page52(self):
        self.add_contact_page("data52")

    def test_validate_contact_details(self):
        data2 = read_data()
        data = data2["data17"]
        self.c.click_contact_details()
        time.sleep(5)

        assert self.c.get_first_name() == data["fname"]
        assert self.c.get_last_name() == data["lname"]
        assert self.c.get_dob() == data["dob"]
        assert self.c.get_email() == data["email"]
        assert self.c.get_phone_number() == data["phone_number"]
        assert self.c.get_address1() == data["adress1"]
        assert self.c.get_address2() == data["adress2"]
        assert self.c.get_city() == data["city"]
        assert self.c.get_post_code() == data["post_code"]
        assert self.c.get_state() == data["state"]
        assert self.c.get_country() == data["country"]

    def test_delete(self):
        self.c.click_table()

        # self.c.return_to_contact_list()
        # self.c.click_table()
