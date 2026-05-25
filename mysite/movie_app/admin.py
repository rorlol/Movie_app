from django.contrib import admin
from .models import UserProfile,Country,Director,Genre,Actor,Movie,MovieLanguages,MovieMoments,Review,Favorite



class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1

class MovieMomentsInline(admin.TabularInline):
    model = MovieMoments
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieLanguagesInline,MovieMomentsInline]





admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie, MovieAdmin)
#admin.site.register(MovieLanguages)
#admin.site.register(MovieMoments)
admin.site.register(Review)
admin.site.register(Favorite)