from app.models import Careers

from rest_framework import serializers

class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = ('id', 'username', 'created_datetime', 'title', 'content')