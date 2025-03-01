from django.urls import path
from .views import PostList, getAllPosts, postDetails, addPost, update_post, delete_post, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', getAllPosts, name='posts'),
    path('<int:post_id>/create/', postDetails, name='postDetails'),
    path('add/', addPost, name='addpost'),
    path('<int:post_id>/update/', update_post, name='update'),
    path('<int:post_id>/delete/', delete_post, name='delete'), 

    ## AUTHENTIFICATION'S LINKS ###
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'authentification/logout.html'), name='logout'),
    path('register/', signup, name='signup'),

    # API ENDPOINTS
    path('api/all/', PostList.as_view())
]
