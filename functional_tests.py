import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):

        # navigate to brower
        self.browser.get('http://localhost:8080')

        # check the title includes browser
        self.assertIn('To-Do Lists', self.browser.title)


if __name__ == '__main__':
    unittest.main()
