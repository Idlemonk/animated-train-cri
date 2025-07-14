from django.contrib import admin
from .models import RecoveryRequest, Contact

# Register your models here.
admin.site.register([RecoveryRequest, Contact])
