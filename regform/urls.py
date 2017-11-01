from django.conf.urls import url

from . import views

app_name = 'regform'

urlpatterns = [
    url(r'^$', views.register_member),
    # url(r'^registration-form/registered$', views.registered)
]