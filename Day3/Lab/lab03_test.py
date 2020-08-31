import unittest
from lab03 import *

class MyTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout('Keenan'), 'KEENAN')
        self.assertEqual(shout('Alper'), 'ALPER')
        self.assertEqual(shout('Gechun'), 'GECHUN')
        self.assertEqual(shout('Dahjin'), 'DAHJIN')

    def test_reverse(self):
        self.assertEqual(reverse('Keenan'), 'naneeK')
        self.assertEqual(reverse('Alper'), 'replA')
        self.assertEqual(reverse('nuhceG'), 'Gechun')
        self.assertEqual(reverse('JIN'), 'NIJ')

    def test_reversewords(self):
        self.assertEqual(reversewords('cool is Patrick'), 'Patrick is cool')

    def test_reversewordletters(self):
        self.assertEqual(reversewordletters('dooG gninroM'), 'Good Morning')

    def test_piglatin(self):
        self.assertEqual(piglatin('Keenan'), 'eenan-kay')
        self.assertEqual(piglatin('Alper'), 'alper-yay')
        self.assertEqual(piglatin('Gechun'), 'echun-gay')
        self.assertEqual(piglatin('Dahjin'), 'ahjin-day')


if __name__ == '__main__':
    unittest.main()
