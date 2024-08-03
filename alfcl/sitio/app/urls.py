# app/urls.py
from django.urls import path
from .views import home, github, quien_soy, contacto, blog, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('github/', github, name='github'),
    path('quien-soy/', quien_soy, name='quien_soy'),
    path('contacto/', contacto, name='contacto'),
    path('blog/', blog, name='blog'),
    path('blog/<str:filename>/', post_detail, name='post_detail'),
]