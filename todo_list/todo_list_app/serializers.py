from django.contrib.auth.models import User
from rest_framework import serializers
from . models import ToDo

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class TasksSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = ToDo
        fields = ['user', 'task', 'time_stamp', 'is_done']
