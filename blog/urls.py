from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    # blog/
    path('', views.PostList.as_view(), name='post_list'),
]