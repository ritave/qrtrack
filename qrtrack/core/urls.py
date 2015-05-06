from django.conf.urls import url, include
from django.contrib import admin
import qrtrack.core.views as views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
]
