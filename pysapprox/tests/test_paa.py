import unittest
import pysapprox
import numpy as np


class paaTest(unittest.TestCase):
    def setUp(self):
        print("setUp executed!")

    def testpaaConversion(self):
        T = np.linspace(0, 10, 1000)
        paa1 = pysapprox.paa(T,1000)

        np.testing.assert_equal(np.size(paa1), 1000)
        paa2 = pysapprox.paa(T, 10)
        np.testing.assert_equal(np.size(paa2), 10)


if __name__ == "__main__":
    unittest.main()
