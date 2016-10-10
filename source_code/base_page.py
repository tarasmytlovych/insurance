from library.webdriver_provider import WebDriverProvider
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver=None, ia_url="http://ia.ca/individuals"):
        self.driver = driver if driver else WebDriverProvider.get_driver(URL=ia_url)

    def wait_for_visibility_of_element(self, locator):
        return WebDriverWait(driver=self.driver, timeout=20)\
            .until(EC.visibility_of_element_located(locator=locator))



            #.until(EC.visibility_of_element_located(locator = locator))

