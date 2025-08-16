from rest_framework import serializers
from myapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stduent
        fields='__all__'
        # exclude=['name']

class EmpSerializer(serializers.ModelSerializer):
    class Meta :
        model=Emp
        fields='__all__'

    def validate(self, attrs):
        if attrs['salary'] <5000:
            raise serializers.ValidationError("Salary must be grater than 5000")
        
        return attrs