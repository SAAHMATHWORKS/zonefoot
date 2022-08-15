from django.urls import path
from coupe import views

urlpatterns = [
    path('', views.coupe, name='coupe'),
]