from rest_framework import serializers
from .models import UserProfile,Country,Director,Genre,Actor,Movie,MovieLanguages,MovieMoments,Review,Favorite



class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username']

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['id','title','video']


class MovieListSerializers(serializers.ModelSerializer):
    #director = DirectorSerializers(many=True)
    country = CountrySerializers(many=True)
    class Meta:
        model = Movie
        fields = ['id','movie_image','movie_name','release_date','country']

class ReviewSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    movie = MovieListSerializers()

    class Meta:
        model = Review
        fields = '__all__'

class MovieDetailSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True)
    director = DirectorSerializers(many=True)
    genre = GenreSerializers(many=True)
    actor = ActorSerializers(many=True)
    movie_languages = MovieLanguagesSerializers(read_only=True, many=True)
    reviews = ReviewSerializers(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['id','movie_image','movie_trailer','movie_name','release_date','country',
                  'director','genre','type_quality','movie_time','actor','description','movie_languages',
                  'reviews']

class MovieMomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieMoments
        fields = '__all__'

class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'