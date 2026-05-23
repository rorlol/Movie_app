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
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(12), MaxValueValidator(75)])
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='simple')

class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

class Director(models.Model):
    director_name = models.CharField(max_length=32)
    director_image = models.ImageField(upload_to='director_images/')
    bio = models.TextField()

class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)

class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    actor_image = models.ImageField(upload_to='actor_images/')
    bio = models.TextField()

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
    type_quality = models.Choices(max_lenght=4, choices=TYPE_CHOICES)
    movie_time = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='simple')

class MovieLanguages(models.Model):
    model = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    video = models.FileField(upload_to='movie_videos/')

class MovieMoments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    moments_image = models.ImageField(upload_to='movie_moments_images/', null=True, blank=True)
    moments_video = models.FileField(upload_to='movie_moments_videos/', null=True, blank=True)

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    stars = models.PositiveSmallIntegerField(choices=[(i,str (i)) for i in range(1,11)], null=True, blank=True)

class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)