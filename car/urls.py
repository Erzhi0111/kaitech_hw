from django.urls import path
from .views import CarListCreateView, CarDetailView

urlpatterns = [
    path('car/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]