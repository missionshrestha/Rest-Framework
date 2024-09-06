from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    """
    Serializer for the Student model.

    Attributes:
        name (CharField): The name of the student.
        roll (IntegerField): The roll number of the student.
        city (CharField): The city of the student.

    Methods:
        create(validated_data): Creates a new student instance with the validated data.
    """
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """
        Creates a new student instance with the validated data.

        Args:
            validated_data (dict): The validated data containing the field values.

        Returns:
            Student: The newly created student instance.
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates the fields of the given instance with the validated data.

        Args:
            instance: The instance to be updated.
            validated_data: The validated data containing the updated field values.

        Returns:
            The updated instance.
        """
        print(instance)
        instance.name = validated_data.get('name', instance.name)
        print(instance)         
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance