from rest_framework.generics import ListAPIView, RetrieveAPIView
from topics_list.models import TopicsList
from .serializers import TopicsListSerializer


class TopicsListView(ListAPIView):
    queryset = TopicsList.objects.all()
    serializer_class = TopicsListSerializer


class TopicsDetailView(RetrieveAPIView):
    queryset = TopicsList.objects.all()
    serializer_class = TopicsListSerializer