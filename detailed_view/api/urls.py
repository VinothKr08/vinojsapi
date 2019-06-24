
from django.urls import path
from .views import DetailView


urlpatterns = [

    path('<title>/', DetailView.as_view()),
]

