from django.urls import path
from .views import videoListView,VideoDetailView,VideoCreateView

app_name = 'videoDetails'

urlpatterns = [
    path('',videoListView.as_view(),name='list'),
    path('detail/<slug>/',VideoDetailView.as_view(),name='detail'),
    path('create/',VideoCreateView.as_view(),name='create'),
    
]