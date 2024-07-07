# community/serializers.py
from rest_framework import serializers
from .models import User, Board, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = '__all__'

    def get_nickname(self, obj):
        return User.objects.get(user_id=obj.writer_id).nickname

class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_nickname(self, obj):
        return User.objects.get(user_id=obj.writer_id).nickname

class BoardDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = '__all__'

    def get_nickname(self, obj):
        return User.objects.get(user_id=obj.writer_id).nickname
