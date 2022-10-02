from pyexpat import model
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.Serializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rater(self, obj):
        return obj.rater.username

    def get_agent(self, obj):
        return obj.agent.user.username
