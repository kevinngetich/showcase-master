from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'kevinngetich'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    #url(r'', views.login.as_view(), name='login'),
    url(r'^feed/', include('feed.urls'), name='feed'),

    #url(r'^login/$', views.Home.as_view, name='login'),
    #url('', views.home.as_view(), name='home'),
    #url(r'^auth/', include('social_django.urls', namespace='social')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)