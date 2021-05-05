from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>>/', views.post_detail, name='post_detail'),
    
]
def post_detail(request, pk):
    Post.objects.get(pk=pk)