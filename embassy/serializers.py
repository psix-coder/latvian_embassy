from rest_framework import serializers
from .models import Meeting, Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'slug']


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ['id', 'customer', 'meet_time', 'service']