from django.conf.urls import url
import qrtrack.core.views as views

urlpatterns = [
    url(r'^$', views.test)
]
