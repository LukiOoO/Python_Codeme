import unittest
from area import rectangle, triangle, is_active, trapezoid


class AreasTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 4
        self.b = 6

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 24)

    def test_triangle_correct_values(self):
        result = triangle(4, 4)
        self.assertEqual(result, 8)

    def test_dummy(self):
        self.assertNotEqual(9, 11)
        state = not is_active()
        self.assertFalse(state)

    def test_triangle_with_incorrect_values(self):
        self.assertRaises(ValueError, triangle(4, "#@#@"))

    def test_rectangle_with_incorrect_values(self):
        #self.assertRaises(ValueError, rectangle(4, "@@"))

        with self.assertRaises(ValueError):
            rectangle(4, "@@@$#")


    def tearDown(self):
        del self.a
        del self.b

    def trapezoid_with_correct_valeues(self):
        result = trapezoid(self.a, self.b, 5)
        self.assertEqual(result, 25)

    def trapezoid_with_incorrect_valeues(self):
        with self.assertRaises(ValueError):
            trapezoid(4, "@@@$#", "__=")


if __name__ == "__main__":
    unittest.main()
