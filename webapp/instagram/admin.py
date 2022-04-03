from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models
# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'photo_tag', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def message_length(self, post):
        return f'{len(post.message)} 글자'

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src={post.photo.url} style="width: 50px;"/>')

        return None