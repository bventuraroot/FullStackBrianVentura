from rest_framework import serializers
from .models import Bookings, Courts, Frecuency, States, Partners, Tutorial


class courts_serializer(serializers.ModelSerializer):
    class Meta:
        model = Courts
        #fields = ['courts_id', 'courts_name', 'courts_descripcion', 'courts_location', 'courts_picture', 'courts_state']
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'title', 'description', 'published')

class Partners_serializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('__all__')
