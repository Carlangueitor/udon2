from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    synopsis = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='animes', blank=True, null=True)
    genres = models.ManyToManyField('Genre')
    demographics = models.ManyToManyField('Demographic')
    alternative_titles = models.ManyToManyField('Title')

    def __unicode__(self):
        return self.title


class Title(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class Serie(Anime):
    episodes = models.ManyToManyField('Episode')


class Episode(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="episodes", blank=True, null=True)
    number = models.IntegerField()
    date_aired = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.number


class Movie(Anime):
    pass


class OAD(Anime):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="categories", blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Genre(Category):
    pass


class Demographic(Category):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.name
