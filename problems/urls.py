
from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^Set1/([1-8]{1})', views.set_one_dispatcher, name='set_one_dispatcher'),
        url(r'^Set1/$', views.set_one),
    ]
