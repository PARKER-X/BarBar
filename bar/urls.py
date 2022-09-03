from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('face/',views.face, name='face' ),
   path('predict', views.predict, name='predict'),
   path('diamond', views.diamond, name='diamond'),
   path('triangle', views.triangle, name='triangle'),
   path('square', views.square, name='square'),
   path("round", views.round, name='round'),
   path("oval", views.oval, name='oval'),
   path("oblong", views.oblong, name='oblong'),
   path("heart", views.heart, name='heart'),
   
]
