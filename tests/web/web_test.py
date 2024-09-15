import pytest
from time import sleep
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.login_page import RegisterPage
from tests.web.pages.login_page import CalcPage
from assertpy import assert_that


class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        assert_that(LoginPage(self.driver).elements.username_logged_in.text).is_equal_to('admin')
        a = 1

# class TestReg(WebBase):
    
    def test_register(self):
        RegisterPage(self.driver).elements.register.click()
        RegisterPage(self.driver).elements.username.set('plupp')
        RegisterPage(self.driver).elements.password1.set('test1234')
        RegisterPage(self.driver).elements.password2.set('test1234')
        RegisterPage(self.driver).elements.register.click()
        assert_that(RegisterPage(self.driver).elements.username_registered.text).is_equal_to('User already exists!')
        # assert_that(RegisterPage(self.driver).elements.username_logged_in.text).is_equal_to(unique_username)
        a = 2

    def test_calc_e2e(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        CalcPage(self.driver).elements.login.click()
        CalcPage(self.driver).elements.key1.click()
        CalcPage(self.driver).elements.keyadd.click()
        CalcPage(self.driver).elements.key2.click()
        CalcPage(self.driver).elements.keyequals.click()
        assert_that(CalcPage(self.driver).elements.summa.value).is_equal_to('3')
        CalcPage(self.driver).elements.keyclear.click()
        CalcPage(self.driver).elements.key5.click()
        CalcPage(self.driver).elements.keysub.click()
        CalcPage(self.driver).elements.key3.click()
        CalcPage(self.driver).elements.keyequals.click()
        assert_that(CalcPage(self.driver).elements.summa.value).is_equal_to('2')
        CalcPage(self.driver).elements.keyclear.click()
        CalcPage(self.driver).elements.key6.click()
        CalcPage(self.driver).elements.keydiv.click()
        CalcPage(self.driver).elements.key2.click()
        CalcPage(self.driver).elements.keyequals.click()
        assert_that(CalcPage(self.driver).elements.summa.value).is_equal_to('3')
        CalcPage(self.driver).elements.keyclear.click()
        CalcPage(self.driver).elements.key2.click()
        CalcPage(self.driver).elements.keymulti.click()
        CalcPage(self.driver).elements.key2.click()
        CalcPage(self.driver).elements.keyequals.click()
        assert_that(CalcPage(self.driver).elements.summa.value).is_equal_to('4')

        a = 3

    def test_calc_history(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        CalcPage(self.driver).elements.login.click()

        CalcPage(self.driver).elements.key1.click()
        CalcPage(self.driver).elements.keyadd.click()
        CalcPage(self.driver).elements.key2.click()
        CalcPage(self.driver).elements.keyequals.click()
        CalcPage(self.driver).elements.keyclear.click()

        CalcPage(self.driver).elements.key6.click()
        CalcPage(self.driver).elements.keydiv.click()
        CalcPage(self.driver).elements.key2.click()
        CalcPage(self.driver).elements.keyequals.click()

        CalcPage(self.driver).elements.historybutton.click()

        assert_that(CalcPage(self.driver).elements.historypanel.value).is_equal_to('1+2=3\n6/2=3\n')
        a = 3