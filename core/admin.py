from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(CustumUser, UserAdmin)
admin.site.register(StyledImageCollection)
admin.site.register(StyleImageCollection)
admin.site.register(StyleImage)
admin.site.register(OriginalImage)
admin.site.register(StyledImage)
