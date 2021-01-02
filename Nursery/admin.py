from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Plant)
admin.site.register(models.NurseryPlant)
admin.site.register(models.NurseryDetails)
admin.site.register(models.Cart)