from django.contrib import admin
from .models import Post,tags,User

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(User)
admin.site.register(Post,PostAdmin)
admin.site.register(tags)
