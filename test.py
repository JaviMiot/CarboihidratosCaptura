import unittest
from selenium import webdriver
from fundation import Fundation


class TestFundation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get(self.fundation.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.fundation = Fundation(self.driver)

    def test_change_group(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
