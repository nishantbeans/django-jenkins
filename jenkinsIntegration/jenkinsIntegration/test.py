from django.test import TestCase

class BasicTestCase(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 4)

    def test_sub(self):
        self.assertEqual(5 - 2, 4)