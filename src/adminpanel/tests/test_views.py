from django.test import SimpleTestCase
from django.test.client import RequestFactory

from adminpanel.views import CreateGenre


def setup_view(view, request, *args, **kwargs):
    """
    Prepare view for setup.
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


class AdminTest(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_genre_url(self):
        request = self.factory.get('/admin/add-genre/')
        view = CreateGenre.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
