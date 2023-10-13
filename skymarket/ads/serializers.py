from rest_framework import serializers

from skymarket.ads.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.SlugRelatedField(read_only=True, source='author', slug_field='phone')
    author_first_name = serializers.SlugRelatedField(read_only=True, source='author', slug_field='first_name')
    author_last_name = serializers.SlugRelatedField(read_only=True, source='author', slug_field='last_name')

    class Meta:
        model = Ad
        fields = '__all__'
