from rest_framework import serializers
from detailed_view.models import DetailedView


class DetailedViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedView
        fields = ('title', 'order_no', 'subtitle', 'description', 'example', 'output')
