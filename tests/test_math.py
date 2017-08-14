import unittest

import numpy as np

import syft
from syft import TensorBase


class DotTests(unittest.TestCase):
    def testDotInt(self):
        t1 = TensorBase(np.array([1, 2, 3]))
        t2 = TensorBase(np.array([4, 5, 6]))
        self.assertEqual(syft.dot(t1, t2), 32)

    def testDotFloat(self):
        t1 = TensorBase(np.array([1.3, 2.5, 3.7]))
        t2 = TensorBase(np.array([4.9, 5.8, 6.5]))
        self.assertEqual(syft.dot(t1, t2), 44.92)


class MatmulTests(unittest.TestCase):
    def testMatmul1DInt(self):
        t1 = TensorBase(np.array([1, 2, 3]))
        t2 = TensorBase(np.array([4, 5, 6]))
        self.assertEqual(syft.matmul(t1, t2), syft.dot(t1, t2))

    def testMatmul1DFloat(self):
        t1 = TensorBase(np.array([1.3, 2.5, 3.7]))
        t2 = TensorBase(np.array([4.9, 5.8, 6.5]))
        self.assertEqual(syft.matmul(t1, t2), syft.dot(t1, t2))

    def testMatmul2DIdentity(self):
        t1 = TensorBase(np.array([[1, 0],
                                  [0, 1]]))
        t2 = TensorBase(np.array([[5.8, 6.5],
                                  [7.8, 8.9]]))
        self.assertTrue(syft.equal(syft.matmul(t1, t2), [[5.8, 6.5],
                                                         [7.8, 8.9]]))

    def testMatmul2DInt(self):
        t1 = TensorBase(np.array([[1, 2],
                                  [3, 4]]))
        t2 = TensorBase(np.array([[5, 6],
                                  [7, 8]]))
        self.assertTrue(syft.equal(syft.matmul(t1, t2), [[19, 22],
                                                         [43, 50]]))

    def testMatmul2DFloat(self):
        t1 = TensorBase(np.array([[1.3, 2.5],
                                  [3.4, 4.5]]))
        t2 = TensorBase(np.array([[5.8, 6.5],
                                  [7.8, 8.9]]))
        self.assertTrue(syft.equal(syft.matmul(t1, t2), [[27.04, 30.7],
                                                         [54.82, 62.15]]))


def main():
    unittest.main()


if __name__ == '__main__':
    main()