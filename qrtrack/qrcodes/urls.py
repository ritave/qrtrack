from django.conf.urls import url
import qrtrack.qrcodes.views as view

urlpatterns = [
    url(r'^c/(?P<collect_id>[a-zA-Z0-9]+)$', view.collect, name='collect'),
    url(r'^s/(?P<show_id>[a-zA-Z0-9]+)$', view.show, name='show'),
]
