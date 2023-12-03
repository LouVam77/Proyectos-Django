from django.urls import path
from . import views #(dentro de esto importa esto)

urlpatterns = [
  path('', views.home),
  path('lesson/', views.lesson),
  path('forum/', views.forum, name='forum'),
  path('create_post/', views.create_post, name='create_post'),
  path('view_post/<int:post_id>/', views.view_post, name='view_post'),
]
