from django.views.generic.edit import CreateView

from library.models import Genre


class CreateGenre(CreateView):
    model = Genre
    template_name = 'base.html'
