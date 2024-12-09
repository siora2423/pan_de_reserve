from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('nyuryoku/', views.nyuryoku, name="nyuryoku"),
	path('result/', views.result, name="result"),
    path('add_pan/', views.add_pan, name="add_pan"),
]