from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeListCreateAPIView.as_view()),
    path('position/', views.PositionListCreateAPIView.as_view())
]