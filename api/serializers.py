from rest_framework import serializers
from api.models import MbotData

class MbotDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MbotData
        fields = ('id', 'timestamp', 'temperature', 'battery', 'sensor_state', 'humidity')
