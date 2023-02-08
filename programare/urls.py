from django.urls import path
from . import views

urlpatterns = [
    path("", views.programare),
    path("lectii/", views.lectii),
    path("lectii/<int:lesson>/", views.lectie),
]