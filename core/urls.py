from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.blog_index, name="blog_index"),
    path('blog/post/<int:post_id>/', views.blog_post, name='blog_post')
]