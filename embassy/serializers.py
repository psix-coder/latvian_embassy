from rest_framework import serializers
from .models import Meeting, Service

class ServiceSerializer(serializers.ModelSerializer0):
    class Meta:
        model = Service
        fields = ['id', 'title', 'slug']


class MeetingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    servise_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        source='service',
        write_only=True
    )

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Meeting
        fields = ['id', 'customer', 'meet_time', 'service']