from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name="login"),
    path('log', views.log, name="log"),
    path('register', views.register, name="register"),
    path("about", views.about, name="about"),
    path("accomodation", views.accomodation, name="accomodation"),
    path("blog", views.blog, name="blog"),
    path("gallery", views.gallery, name="gallery"),
    path("contact", views.contact, name="contact"),
    path("bookingform", views.bookingform, name="bookingform"),
    path("logout", views.logout, name="logout"),
    ]