from rest_framework import serializers

from .models import Employee, Position


class PositionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    position = serializers.CharField()
    department = serializers.CharField()

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.position = validated_data['position']
        instance.department = validated_data['department']
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField()
    year = serializers.DateField()
    salary = serializers.DecimalField(max_digits=19, decimal_places=10)
    job_title = serializers.CharField(max_length=20)


    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ful_name = validated_data['ful_name']
        instance.year = validated_data['year']
        instance.salary = validated_data['salary']
        instance.job_title = validated_data['job_title']
        instance.save()
        return instance
