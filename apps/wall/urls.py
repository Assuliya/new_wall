from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^register$', views.register, name='register'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^show$', views.show, name='show'),
    url(r'^edit$', views.edit, name='edit'),

  ]
