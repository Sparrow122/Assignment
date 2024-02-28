from rest_framework import serializers


class ExperienceSerializer(serializers.Serializer):
    designation = serializers.CharField()
    company = serializers.CharField()

class EducationSerializer(serializers.Serializer):
    institute = serializers.CharField()
    course = serializers.CharField()

class MyDataSerializer(serializers.Serializer):
    name = serializers.CharField()
    about = serializers.CharField()
    headline = serializers.CharField()
    experience = ExperienceSerializer(many=True)
    education = EducationSerializer(many=True)