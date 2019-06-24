from rest_framework import serializers


from topics_list.models import TopicsList


class TopicsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicsList
        fields = ('topic_no', 'title')
