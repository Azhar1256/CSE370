from django.contrib import admin
from .models import VaccineRegistration
from .models import Notices

# Register your models here.
admin.site.register(VaccineRegistration)
admin.site.register(Notices)