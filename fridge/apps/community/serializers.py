# community/serializers.py
from rest_framework import serializers
from .models import User, Board, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    writer_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = '__all__'

    def get_writer_nickname(self, obj):
        try:
            return User.objects.get(user_id=obj.writer_id).nickname
        except User.DoesNotExist:
            return None

class CommentSerializer(serializers.ModelSerializer):
    writer_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_writer_nickname(self, obj):
        try:
            return User.objects.get(user_id=obj.writer_id).nickname
        except User.DoesNotExist:
            return None

class BoardDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    writer_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = '__all__'

    def get_writer_nickname(self, obj):
        try:
            return User.objects.get(user_id=obj.writer_id).nickname
        except User.DoesNotExist:
            return None

    def get_comments(self, obj):
        comments = Comment.objects.filter(board_id=obj.board_id)
        return CommentSerializer(comments, many=True).data
