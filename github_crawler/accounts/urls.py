from django.urls import path
from . import views
urlpatterns = [
    path('',views.github_auth, name=''),
    path('a',views.read_from_csv,name='a'),
]
