from Page.automating_webshop import AutomatingWebShop
from Library.base_fixture import DriverInit


class TestRegister(DriverInit):
    def test_fun(self):
        aw = AutomatingWebShop(self.driver)
        aw.click_reg()
        aw.click_radio()
        aw.enter_first_name()
        aw.enter_last_name()
        aw.enter_email()
        aw.enter_password()
        aw.confirm_password()
        aw.click_register()
