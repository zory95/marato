from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    #path('index2', views.index, name="index"),
    path('', views.index2, name="index2"),
    path('predict', views.predict, name="predict"),
    #path('about/', views.about, name="about"),
    #path('under_construction', views.under_construction, name="under_construction"),
]
