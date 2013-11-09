from django.core.urlresolvers import resolve
from django.test import TestCase

from adminpanel.views import CreateGenre


class AdminTest(TestCase):

    def tesd_add_genre_url(self):
        view = resolve('/admin/add-genre/')
        self.assertEqual(view, CreateGenre)
