from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('opportunities', views.opportunities, name='opportunities'),
    path('send_mail_frontend', views.email_frontend, name='frontend'),
    path('send_mail_backend', views.email_backend, name='backend'),
    path('send_mail_fullstack', views.email_fullstack, name='fullstack'),
]