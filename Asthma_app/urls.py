from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^home$', views.home, name='home'),
	url(r'^visitor', views.user, name='user'),
	url(r'^index', views.index, name='index'),
	url(r'.well-known/acme-challenge', views.ssl, name='ssl'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)