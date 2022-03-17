from rest_framework import serializers


class Employeeserilizer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rollno = serializers.IntegerField()
    designation = serializers.CharField(max_length=100)