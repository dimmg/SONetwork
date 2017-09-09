from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'author', 'created_at', 'updated_at')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.rating()

        return repr
