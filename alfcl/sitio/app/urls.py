from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('github/', views.github, name='github'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('quien-soy/', views.quien_soy, name='quien_soy'),
]