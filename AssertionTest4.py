import unittest

class Test(unittest.TestCase):
    def testName(self):
        list={"python", "selenium", "java"}
        # assert In
        self.assertIn("python", list) #passed
        #self.assertIn("ruby", list)   #failed
        # assert Not In
        self.assertNotIn("ruby", list)    #passed
        #self.assertNotIn("python", list)  #failed

if __name__ == "__main__":
    unittest.main()