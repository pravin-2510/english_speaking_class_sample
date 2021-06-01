from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
from .models import Enquire
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','contact_date','contact_time')
    list_filter = ('contact_date',)


class EnquireAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','contact_date','contact_time')
    list_filter = ('contact_date',)
    
    




# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Enquire, EnquireAdmin)
admin.site.site_header = 'Extreme Spoken English Class Admin'


