from django.test import TestCase


class TestCoachListViews(TestCase):
    def test_coach_list(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
