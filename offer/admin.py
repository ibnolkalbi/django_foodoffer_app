from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ('id','password', 'reasturantName', 'dishName', 'description', 'price', 'image')



