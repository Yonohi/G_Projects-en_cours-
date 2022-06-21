from django.urls import path
from . import views

app_name = 'gestion'
urlpatterns = [
    path("", views.home_view, name="home"),
    path("projet/<str:code_campagne>/", views.detail_view, name='detail'),
    path("nouveau_projet/", views.new_project, name='new'),
]
