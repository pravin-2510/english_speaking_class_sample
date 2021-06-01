from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('sno','title','Created_date')
    list_filter = ('Created_date',)
    search_fields = ('title',)

# Register your models here.
admin.site.register(Post, PostAdmin)