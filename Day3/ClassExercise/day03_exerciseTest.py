import unittest
from day03_exercise import *

class MyTest(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels('KeeNAn'), 3)
        self.assertEqual(count_vowels('alpEr'), 2)
        self.assertEqual(count_vowels('GEchun'), 2)
        self.assertEqual(count_vowels('JIN'), 1)

#	def test_split(self):
#		s = 'hello world'
#		self.assertEqual(s.split(), ['hello', 'world'])
#		# check that s.split fails when the separator is not a string
#		with self.assertRaises(TypeError): # with is the keyword
#			s.split(2)

if __name__ == '__main__':
    unittest.main()
