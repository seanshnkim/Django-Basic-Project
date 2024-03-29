from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('', views.index),
    path('', views.PostList.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('create_post/', views.PostCreate.as_view()),
]