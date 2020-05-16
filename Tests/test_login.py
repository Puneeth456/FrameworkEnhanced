from Pages.LoginPage import Login
import pytest
from Data.Testdata import *


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_fbpage(self):
        driver=self.driver
        lg=Login(driver)
        lg.enter_un()
        lg.enter_pwd()
        lg.click()