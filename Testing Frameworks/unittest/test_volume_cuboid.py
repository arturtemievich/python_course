import unittest
from volume_cuboid import *

# METHOD: assertAlmostEqual
# DESCRIPTION: Method will check whether the output your function gives is equal to what you expect.

# # Example 1: assertAlmostEqual (all testcases are OK)
# class TestCuboid(unittest.TestCase):
#     def test_volume(self):
#         self.assertAlmostEqual(cuboid_volume(2), 8)
#         self.assertAlmostEqual(cuboid_volume(1), 1)
#         self.assertAlmostEqual(cuboid_volume(0), 0)
#         self.assertAlmostEqual(cuboid_volume(5.5), 166.375)


# Example 2: assertAlmostEqual (one of the assertAlmostEqual methods fails)
# class TestCuboid(unittest.TestCase):
#     def test_volume(self):
#         self.assertAlmostEqual(cuboid_volume(2), 8)
#         self.assertAlmostEqual(cuboid_volume(1), 1)
#         self.assertAlmostEqual(cuboid_volume(0), 0)
#         self.assertAlmostEqual(cuboid_volume(5.5), 0)


# METHOD: assertRaises
# DESCRIPTION: Method will help you in finding out whether your function handles the input values correctly.

# Example 3: assertRaises
# class TestCuboid(unittest.TestCase):
#     def test_volume(self):
#         self.assertAlmostEqual(cuboid_volume(2), 8)
#         self.assertAlmostEqual(cuboid_volume(1), 1)
#         self.assertAlmostEqual(cuboid_volume(0), 0)
#
#     # def test_input_value_1(self):
#     #     self.assertRaises(TypeError, cuboid_volume, True)
#
#     def test_input_value_2(self):
#         self.assertRaises(TypeError, cuboid_volume_2, True)


# Example 4: assertRaises
# It is important to know that your test methods inside the Class TestCuboid should start with a keyword 'test'.
# class TestCuboid(unittest.TestCase):
#     def test_volume(self):  # def volume(self):
#         self.assertAlmostEqual(cuboid_volume(2), 8)
#         self.assertAlmostEqual(cuboid_volume(1), 1)
#         self.assertAlmostEqual(cuboid_volume(0), 0)
#
#     def test_input_value_2(self):
#         self.assertRaises(TypeError, cuboid_volume_2, True)


# Reference:
# Unit Testing in Python, www.datacamp.com
