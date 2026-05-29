from random import choices

from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator


STATUS_CHOICES = (
('pro','pro'),
('simple','simple')
)

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', default='+996')
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(12), MaxValueValidator(75)],default=0)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='simple')

class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name

class Director(models.Model):
    director_name = models.CharField(max_length=32)
    director_image = models.ImageField(upload_to='director_images/')
    bio = models.TextField()

    def __str__(self):
        return self.director_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.genre_name

class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    actor_image = models.ImageField(upload_to='actor_images/')
    bio = models.TextField()

    def __str__(self):
        return self.actor_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=32)
    movie_image = models.ImageField(upload_to='movie_images/')
    movie_trailer = models.FileField(upload_to='movie_trailers/')
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
    TYPE_CHOICES = (
    ('1080','1080'),
    ('720','720'),
    ('480','480'),
    ('360','360')
    )
    type_quality = models.CharField(max_length=4, choices=TYPE_CHOICES)
    movie_time = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.movie_name

class MovieLanguages(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='movie_languages')
    title = models.CharField(max_length=32)
    video = models.FileField(upload_to='movie_videos/')

class MovieMoments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    moments_image = models.ImageField(upload_to='movie_moments_images/', null=True, blank=True)
    moments_video = models.FileField(upload_to='movie_moments_videos/', null=True, blank=True)

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='reviews')
    comment = models.TextField(null=True, blank=True)
    stars = models.PositiveSmallIntegerField(choices=[(i,str (i)) for i in range(1,11)], null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.movie}'

class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)