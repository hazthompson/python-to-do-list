from django.http import HttpRequest
from django.test import TestCase

from lists.views import home_page


# Create your tests here.


class HomepageTest(TestCase):
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
