from django.conf.urls import include, url
from django.contrib import admin

import qrtrack.core.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(qrtrack.core.urls))
]
