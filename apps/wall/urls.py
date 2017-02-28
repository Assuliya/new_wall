from django.conf.urls import url
from . import views
from .views import Form
from .forms import RegisterForm, LoginForm


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', Form.as_view(form_action = 'login', form_type = LoginForm), name='login'),
    url(r'^register$', Form.as_view(form_action = 'register', form_type = RegisterForm), name='register'),

    url(r'^admin$', views.admin, name='admin'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^show/(?P<user_id>\d+)$', views.show, name='show'),
    url(r'^edit/(?P<user_id>\d+)$', views.edit, name='edit'),

    url(r'^logout$', views.logout, name='logout'),
    url(r'^delete/(?P<user_id>\d+)$', views.delete, name='delete'),

    url(r'^add_post$', views.add_post, name='add_post'),
    url(r'^delete_post/(?P<post_id>\d+)$', views.delete_post, name='delete_post'),
    url(r'^add_comment/(?P<post_id>\d+)$', views.add_comment, name='add_comment'),
    url(r'^delete_comment/(?P<comment_id>\d+)$', views.delete_comment, name='delete_comment'),

  ]
