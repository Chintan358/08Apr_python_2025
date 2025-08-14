from rest_framework import serializers
from myapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stduent
        fields='__all__'
        # exclude=['name']