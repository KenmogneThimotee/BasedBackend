from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Image)
admin.site.register(Post)
admin.site.register(ClickForStyle)
admin.site.register(PostComment)
admin.site.register(UpVote)
admin.site.register(DownVote)
admin.site.register(LikeComment)
admin.site.register(DislikeComment)
