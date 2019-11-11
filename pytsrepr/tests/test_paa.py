import unittest
import pytsrepr
import numpy as np


class paaTest(unittest.TestCase):
    def setUp(self):
        print("setUp executed!")

    def testPAAConversion(self):
        T = np.linspace(0, 10, 1000)
        paa1 = pytsrepr.paa(T,1000)

        np.testing.assert_equal(np.size(paa1), 1000)
        paa2 = pytsrepr.paa(T, 10)
        np.testing.assert_equal(np.size(paa2), 10)


if __name__ == "__main__":
    unittest.main()
