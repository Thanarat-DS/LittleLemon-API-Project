from django.urls import path
from . import views

urlpatterns = [
    path('groups/managers/users', views.ManagerOnlyView.as_view()),
]