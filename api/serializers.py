from rest_framework import serializers
from rest_framework.response import Response


class PasswordResetSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return Response(status=201)
