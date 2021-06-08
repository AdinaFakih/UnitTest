import unittest
class Test(unittest.TestCase):
    def testName(self):
        # assert greater
        self.assertGreater(1000, 10)
        # assert greater or equal
        self.assertGreaterEqual(1000, 10)
        # assert Less
        self.assertLess(100, 10000)
        self.assertLessEqual(10, 10)

if __name__ == "__main__":
    unittest.main()