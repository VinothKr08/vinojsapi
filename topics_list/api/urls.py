
from django.urls import path
from .views import TopicsListView, TopicsDetailView


urlpatterns = [
    path('', TopicsListView.as_view()),
    path('<pk>', TopicsDetailView.as_view()),
]

