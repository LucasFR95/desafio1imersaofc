from django.contrib import admin

from core.models import Post, Tag



# Register your models here.


class PostAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass



admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)



