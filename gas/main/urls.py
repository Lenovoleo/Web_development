from django.urls import path
from . import views
urlpatterns = [


    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('komanda', views.komanda, name='komanda'),
    path('database', views.database, name='database')
]