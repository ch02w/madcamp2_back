from django.urls import path
from .views import BoardListCreateAPIView, BoardDetailAPIView, CommentCreateAPIView, CommentDeleteAPIView

urlpatterns = [
    path('posts/', BoardListCreateAPIView.as_view(), name='board-list-create'),
    path('posts/<int:board_id>/', BoardDetailAPIView.as_view(), name='board-detail'),
    path('comments/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comments/<int:comment_id>/', CommentDeleteAPIView.as_view(), name='comment-delete'),
]
