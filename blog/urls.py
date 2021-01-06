from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Post views
    #path('', views.post_list, name='post_list'), #We only comment this to check the Class-Based view
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]