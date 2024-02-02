from django.contrib import admin

from accounts.models import User

# Register your models here.
class AbstractAdmin(admin.ModelAdmin):
    list_display=['email','is_superuser','username']
    
admin.site.register(User,AbstractAdmin)