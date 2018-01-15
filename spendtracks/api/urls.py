from django.conf.urls import url

from .core import views

urlpatterns = [
    url(r'^users/create$', views.UserCreate.as_view(), name='users/create'),
]
