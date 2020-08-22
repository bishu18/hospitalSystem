from rest_framework import serializers

from .models import Patient

class PatientSerializer(serializers.Serializer):
    class Meta:
        model = Patient
        field = ('id', 'registered')