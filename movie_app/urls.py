from django.urls import path
from . import views
app_name='movie_app' #namespace
urlpatterns = [

    path('',views.demo,name='demo'),


]
