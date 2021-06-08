import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage = driver.title
        #assertEqual
        self.assertEqual("Google", titleOfWebPage ,"Webpage title is not same")

        # assert Not Equal
        self.assertNotEqual("Google123", titleOfWebPage) #Both are not same

if __name__ == "__main__":
    unittest.main()