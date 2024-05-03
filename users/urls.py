from django.urls import path, include
from .views import RegisterView, LoginView, FollowerUpdateView,  PostListCreateView, PostDetailView, CommentDetailView, CommentListCreateView, LikeCreateView, LikeDetailView, FollowerCreateView, FollowerDetailView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/',PostDetailView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:id>/', CommentDetailView.as_view()),
    path('likes/', LikeCreateView.as_view()),
    path('likes/<int:pk>/', LikeDetailView.as_view()),
    path('followers/', FollowerCreateView.as_view()),
    path('accept/<int:pk>', FollowerUpdateView.as_view()),
    path('followers/<int:id>/', FollowerDetailView.as_view()),
]