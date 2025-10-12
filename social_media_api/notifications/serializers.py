
from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_object = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target_object', 'timestamp']
        read_only_fields = ['id', 'recipient', 'actor', 'actor_username', 'timestamp']

    def get_target_object(self, obj):
        """
        Returns a string representation of the GenericForeignKey target object.
        """
        if obj.target:
            return str(obj.target)
        return None
