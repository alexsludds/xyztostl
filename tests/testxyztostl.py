import unittest

class Testxystostl(unittest.TestCase):

    def test1_triangle(self):
        f = open('test1triangle.txt','r')

        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class Testtxtfile(unittest.TestCase):
    def testtxtfile(self):
        self.

if __name__ == '__main__':
    unittest.main()