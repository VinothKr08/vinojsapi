from rest_framework.generics import ListAPIView
from detailed_view.models import DetailedView
from .serializers import DetailedViewSerializer
from django.shortcuts import get_object_or_404



class DetailView(ListAPIView):
    queryset = DetailedView.objects.all()
    serializer_class = DetailedViewSerializer

    def get_queryset(self):

        title = self.kwargs['title']
        return DetailedView.objects.filter(title=title)
