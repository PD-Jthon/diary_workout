from django.urls import path
from .import views


app_name = 'training_diary'
urlpatterns = [
  path('', views.TopView.as_view(), name='top'),
]