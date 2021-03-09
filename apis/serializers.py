from django.db.models import fields
from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created_at')