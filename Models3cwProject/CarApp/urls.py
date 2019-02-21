from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('all/', views.all, name="index"),
    path('greaterThan2010/', views.greaterThan2010, name="index"),

]


urlpatterns={
    path('', views.index, name="index"),
    path('all/', views.all, name="index"),
    path('add/', views.add, name="index")
}