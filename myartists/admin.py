from django.contrib import admin

from myartists import models


admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.ArtistReview)
