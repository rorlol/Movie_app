from rest_framework import viewsets,generics
from .models import UserProfile,Country,Director,Genre,Actor,Movie,MovieLanguages,MovieMoments,Review,Favorite
from .serializers import (UserProfileSerializers,CountrySerializers,DirectorSerializers,GenreSerializers,
                          ActorSerializers,MovieListSerializers,MovieDetailSerializers,MovieLanguagesSerializers,MovieMomentsSerializers,
                          ReviewSerializers,FavoriteSerializers)
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import MovieFilter
from .pagination import MoviePagination

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    filter_backends = [SearchFilter]
    search_fields = ['director_name']

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers

class MovieListViewSet(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['movie_name']
    ordering_fields = ['movie_time','release_date']
    filterset_class = MovieFilter
    pagination_class = MoviePagination

class MovieDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers

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
