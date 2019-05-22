from django.conf.urls import include
from django.urls import path
from . import views


app_name = 'article'

urlpatterns = [
    path(r'', views.FeedsView.as_view(), name='feed'),
    path(r'<int:pk>', views.DetailView.as_view(), name='details'),
    #url(r'^logout/$', views.logout, name='logout'),
    path(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
]

