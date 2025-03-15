import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        input1 = self.browser.find_element_by_css_selector(
            "[placeholder='Input your first name']"
        )
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_css_selector(
            "[placeholder='Input your last name']"
        )
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_css_selector(
            "[placeholder='Input your email']"
        )
        input3.send_keys("ivan.petrov@example.com")
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text
        )

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        input1 = self.browser.find_element_by_css_selector(
            "[placeholder='Input your first name']"
        )
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_css_selector(
            "[placeholder='Input your last name']"
        )
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_css_selector(
            "[placeholder='Input your email']"
        )
        input3.send_keys("ivan.petrov@example.com")
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text
        )


if __name__ == "__main__":
    unittest.main()
