# This code is used to import  the datas
import pytest

from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestNameSearch:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.WebData().url) # this code is used to get the url from the data
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10) # this code is used to for explicit wait
        yield
        self.driver.quit()



    def clickButton(self,locator):
        self.wait.until(ec.presence_of_element_located((By.XPATH,locator))).click()

    def fillText(self, locator,value):
        self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(value)

    def test_search(self,boot):
        # This code is used to scroll the webpage
            self.driver.execute_script('window.scrollBy(0, 500)')
        # These code is used to click and fill the required data from the data and locator file
            self.clickButton(locator.WebLocator().expandAllLocator)
            self.fillText(locator.WebLocator().nameLocator,data.WebData().name)
            self.fillText(locator.WebLocator().birthdayLocator, data.WebData().birthday)
            try:
                self.clickButton(locator.WebLocator().searchLocator)
            except NoSuchElementException as e:
                print(e)
            # This code is used to check whether the search is done
            if self.driver.current_url == data.WebData().dashboardURL:
                print("Success: URL is valid")
            else:
                print(" error")












