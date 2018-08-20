#!python3
#blogsite_test.py

import unittest

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import bs4, requests


class blogTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome('webdriver path')
        self.driver.get("https://fredricki.github.io")


    def tearDown(self):
        self.driver.quit()


    def test_home_page(self):

        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.title, "Programming to Learn")
        


    def test_about_me(self):
        self.driver.implicitly_wait(10)
        self.about_me = self.driver.find_element_by_xpath("/html/body/aside/div/nav/ul/li[1]/a")
        self.about_me.click()
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.title, "Programming to Learn – About Me")

    def test_contact_page(self):

        
        res = requests.get('https://fredricki.github.io/pages/contact.html#contact')
        contact_soup = bs4.BeautifulSoup(res.text, 'html.parser')
        self.driver.implicitly_wait(10)
        self.contact_page = self.driver.find_element_by_xpath('/html/body/aside/div/nav/ul/li[2]/a')
        self.contact_page.click()
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.title, 'Programming to Learn – Contact')
        self.assertIn('Telephone', contact_soup.text)
        
        



    def test_portfolio(self):

        self.driver.implicitly_wait(10)
        self.portfolio = self.driver.find_element_by_xpath('/html/body/aside/div/nav/ul/li[3]/a')
        self.portfolio.click()
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.title, 'Programming to Learn – My Portfolio')
        
        








if __name__ == "__main__":
    unittest.main()
        
