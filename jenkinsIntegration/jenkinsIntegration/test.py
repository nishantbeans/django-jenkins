from django.test import TestCase
import unittest
import xmlrunner


class BasicTestCase(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 4)

    def test_sub(self):
        self.assertEqual(5 - 2, 4)

    def test_mul(self):
        self.assertEqual(5 * 2, 4)

if __name__ == '__main__':
    with open('/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)