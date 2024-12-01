import unittest
import cal

class TestCal(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cal.add(10, 5), 15)
        self.assertEqual(cal.add(-1, 1), 0)
        self.assertEqual(cal.add(-1, -1), -2)


    def test_subtract(self):
        self.assertEqual(cal.subtract(10, 5), 5)
        self.assertEqual(cal.subtract(-1, 1), -2)
        self.assertEqual(cal.subtract(-1, -1), 0)


    def test_multiply(self):
        self.assertEqual(cal.multiply(10, 5), 50)
        self.assertEqual(cal.multiply(-1, 1), -1)
        self.assertEqual(cal.multiply(-1, -1), 1)


    def test_divide(self):
        self.assertEqual(cal.divide(10, 5), 2)
        self.assertEqual(cal.divide(-1, 1), -1)
        self.assertEqual(cal.divide(-1, -1), 1)

        self.assertRaises(ValueError, cal.divide, 5, 0)

        with self.assertRaises(ValueError):
            cal.divide(-1, 0)




if __name__ == '__main__':
    unittest.main()
