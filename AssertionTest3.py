import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
        #driver = None

        #assert Is None
        self.assertIsNone(driver) #If it have no value then the test case will pass otherwise it will fail

        # assert Is Not None,  means it has some value
        self.assertIsNotNone(driver)
if __name__ == "__main__":
    unittest.main()