from django.test import TestCase

# Create your tests here.


class MainPagesTestCase(TestCase):

    def test_indexpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")
