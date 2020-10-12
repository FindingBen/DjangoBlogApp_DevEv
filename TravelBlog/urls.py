from django.urls import path
from .views import (
    JourneyListView, 
    JourneyDetailView, 
    JourneyCreateView,
    JourneyUpdateView,
    JourneyDeleteView
)
from . import views

urlpatterns = [
    path('', JourneyListView.as_view(), name='TravelBlog-home'),
    path('journey/<int:pk>/', JourneyDetailView.as_view(), name='journey-detail'),
    path('journey/new/', JourneyCreateView.as_view(), name='journey-create'),
    path('journey/<int:pk>/update', JourneyUpdateView.as_view(), name='journey-update'),
    path('journey/<int:pk>/delete', JourneyDeleteView.as_view(), name='journey-delete'),
    path('dashboard/', views.dashboard, name='TravelBlog-dashboard'),
]