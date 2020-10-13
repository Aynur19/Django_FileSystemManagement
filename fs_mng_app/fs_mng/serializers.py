from rest_framework import serializers


class FileInfoListSerializer(serializers.Serializer):
    data = serializers.ListField()


class FileInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    type = serializers.CharField(max_length=128)
    time = serializers.DateTimeField()
