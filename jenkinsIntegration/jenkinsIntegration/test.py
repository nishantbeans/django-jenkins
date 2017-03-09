from django.test import TestCase

class BasicTestCase(TestCase):
    def test_animals_can_speak(self):
        self.assertEqual(1+2, 4)