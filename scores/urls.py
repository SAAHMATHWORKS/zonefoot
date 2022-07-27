from django.urls import path
from scores import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fixtures/', views.fixtures, name='fixtures'),
    path('classement/', views.classement, name='classement'),
    path('fixture_detail/<int:id>/', views.fixture_detail, name='fixture_detail'),
    path('buteurs/', views.clsbuteurs, name='clsbuteurs'),
    path('cartons/', views.cards, name='cards'),
    path('addMessage/', views.addMessage, name='addMessage'),
]