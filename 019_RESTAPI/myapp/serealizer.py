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
    

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'


class BookSerializer(serializers.ModelSerializer):
    # author=AuthorSerializer()
    class Meta:
        model=Book
        fields='__all__'

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        representation['author'] = AuthorSerializer(instance.author).data
       
        return representation