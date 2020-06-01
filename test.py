"""Testing is a method where individual units of source code like functions are tested to see
whether they work properly.

- A Test is simply another python file. There's usually a test file accompanying a file.
- The test file never runs in production, it's file to run the main file before it's released"""
import unittest
import main


class TestMain(unittest.TestCase):  # Unittest works by creating a class and inheriting TestCase from unittest module
    def setUp(self):  # Really useful to setup something before each function e.g variables
        print('About to test a function')

    def test_do_stuff(self):  # We're testing the do_stuff function in the main.py file. We create the method(cause it's in a class)that will receive self
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # This is the key part of unit test. This makes sure that the two parameters are equal

    def test_do_stuff2(self):  # We're testing the do_stuff function in the main.py file. We create the method(cause it's in a
        # class)that will receice self
        test_param = 'hgczvxvjhb'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'put number more than 0')

    def tearDown(self):  # Runs at the end of each method. Can be used to clean up or reset some variables.
    	print('cleaning up')


# You can also do multiple tests by creating more methods in the class. If the main file has more functions


# This usually applies to the main file that is actually going to run the program. It's common practice to do so.

if __name__ == '__main__':
    unittest.main()  # This will run the file to test it. This has nothing to do with main.py
