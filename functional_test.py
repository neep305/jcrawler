from selenium import webdriver
<<<<<<< HEAD
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retriev_it_later(self):
        self.browser.get('http://localhost:8080')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# browser = webdriver.Safari()
# browser.get('http://localhost:8080')

# assert 'Django' in browser.title

# browser.quit()
    if __name__ == '__main__':
        unittest.main(warnings='ignore')
=======

browser = webdriver.Safari()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
>>>>>>> b9537fcd9423db0cb27eb165995d9394271ffa3a
