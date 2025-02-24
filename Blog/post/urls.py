from django.urls import path
from .views import getAllPosts, postDetails, addPost, update_post, delete_post

urlpatterns = [
    path('', getAllPosts, name='posts'),
    path('<int:post_id>/create/', postDetails, name='postDetails'),
    path('add/', addPost, name='addpost'),
    path('<int:post_id>/update/', update_post, name='update'),
    path('<int:post_id>/delete/', delete_post, name='delete')
]
