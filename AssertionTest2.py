import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage = driver.title
        #assert  True
        #self.assertTrue(titleOfWebPage == "Google") #True #if I give "Google123" test case will fail

        # assert False
        self.assertFalse( titleOfWebPage=="Google123") #Negative Test cases, false

if __name__ == "__main__":
    unittest.main()