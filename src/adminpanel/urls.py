from django.conf.urls import patterns, url
from .views import CreateGenre

urlpatterns = patterns('',
    url(r'^add-genre/', CreateGenre.as_view(), name="add_genre"),
)
