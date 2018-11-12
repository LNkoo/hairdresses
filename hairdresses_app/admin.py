from django.contrib import admin
from hairdresses_app.models import Client, Hairdo, AdditionalService, Bill


admin.site.register(Client)
admin.site.register(Hairdo)
admin.site.register(AdditionalService)
admin.site.register(Bill)
