
from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^Set1/', views.set_one),
    ]
