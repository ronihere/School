from django.contrib import admin
from . models import details,notice,to_do,all_urls,upcomingevents

# Register your models here.
admin.site.register(details)
admin.site.register(notice)
admin.site.register(to_do)
admin.site.register(all_urls)
admin.site.register(upcomingevents)