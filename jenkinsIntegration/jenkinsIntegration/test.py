from django.test import TestCase

class BasicTestCase(TestCase):
    def test_addition(self):
        self.assertEqual(1+2, 4)