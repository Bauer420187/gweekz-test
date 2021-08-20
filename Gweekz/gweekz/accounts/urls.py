from django.urls import path
from . import views


urlpatterns = [
    
    path("",views.home, name = "home"),
    path("checkout/", views.checkout, name = "checkout"),
    path("games/",views.games, name = "games"),
    path("login/", views.login, name= "login"),
    path("register/", views.register, name= "register"),
    path("upload/", views.upload, name = "upload")

]
