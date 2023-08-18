from django.contrib import admin

# Register your models here.

from projectapp.models import registrationData
class serviceadmin(admin.ModelAdmin):
    list_display=('name','fname')
admin.site.register(registrationData,serviceadmin)



