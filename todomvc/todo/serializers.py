from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
# could eliminate passwords by selecting fields; all are included here.
