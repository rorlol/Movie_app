from rest_framework import viewsets
from .models import UserProfile,Country,Director,Genre,Actor,Movie,MovieLanguages,MovieMoments,Review,Favorite
from .serializers import (UserProfileSerializers,CountrySerializers,DirectorSerializers,GenreSerializers,
                          ActorSerializers,MovieSerializers,MovieLanguagesSerializers,MovieMomentsSerializers,
                          ReviewSerializers,FavoriteSerializers)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

class MovieLanguagesViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializers

class MovieMomentsViewSet(viewsets.ModelViewSet):
    queryset = MovieMoments.objects.all()
    serializer_class = MovieMomentsSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers
