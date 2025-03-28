from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/register/', views.register, name='register'),
]
    