from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    """
        Create and return a new `Student` instance, given the validated data.

        This method is called when `serializer.save()` is invoked on a serializer
        instance that was initialized with data (i.e., for creating a new object).
        The `save` method internally calls this `create` method if the instance
        does not already exist.
        
        Args:
            validated_data (dict): The validated data from the serializer.

        Returns:
            Student: A new `Student` instance created with the validated data.
        """