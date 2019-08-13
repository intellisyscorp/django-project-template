from django.test import TestCase


class HealthCheckTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = "/health/"

    def test_health_check(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
