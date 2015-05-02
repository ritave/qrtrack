from django.contrib import admin
import qrtrack.qrcodes.models as models

admin.site.register(models.QRCollection)
admin.site.register(models.QRTag)
admin.site.register(models.CompletedTag)
