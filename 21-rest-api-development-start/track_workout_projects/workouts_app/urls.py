from django.urls import path
from .views import ExerviseAPIView

urlpatterns = [
    path('exercises/', ExerviseAPIView.as_view(), name='exercise-list')
]