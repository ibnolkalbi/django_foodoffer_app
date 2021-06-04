from django.contrib import admin
from django.urls import path, include
from offer import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.handlelogin, name="login"),
    path("logout/", views.handlelogout, name="logout"),
    path("post/", views.post, name="post"),
    path("createUser/", views.createUser, name="createUser"),
    path("handlepost/", views.handlepost, name="handlepost"),
    path("login/send/", views.send, name="send"),
    path("/<int:id>/", views.details, name="details"),

    path("<int:id>/", views.postdel, name="postdelete"),
  
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 