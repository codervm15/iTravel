from django.urls import path
from . import views

app_name='Travello'
urlpatterns = [
    path('',views.homepage)
]