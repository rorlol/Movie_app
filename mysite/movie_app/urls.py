from django.urls import path,include
from rest_framework import routers
from .views import (UserProfileViewSet,CountryViewSet,DirectorViewSet,GenreViewSet,ActorViewSet,
                    MovieLanguagesViewSet,MovieMomentsViewSet,ReviewViewSet,FavoriteViewSet,
                    MovieDetailViewSet,MovieListViewSet)

router = routers.DefaultRouter()


router.register(r'user_profile', UserProfileViewSet, basename='user_profile')
router.register(r'country',CountryViewSet , basename='country')
router.register(r'director',DirectorViewSet , basename='director')
router.register(r'genre',GenreViewSet , basename='genre')
router.register(r'actor',ActorViewSet , basename='actor')
#router.register(r'movie',MovieViewSet , basename='movie')
router.register(r'movie_languages',MovieLanguagesViewSet , basename='movie_languages')
router.register(r'movie_moments',MovieMomentsViewSet , basename='movie_moments')
router.register(r'review',ReviewViewSet , basename='review')
router.register(r'favorite',FavoriteViewSet , basename='favorite')



urlpatterns = [
    path('', include(router.urls)),

    path('movie/',MovieListViewSet.as_view(),name='movie_list'),
    path('movie/<int:pk>/',MovieDetailViewSet.as_view(),name='movie_detail')
]
