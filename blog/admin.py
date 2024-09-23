from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','slug','status','created_on')
    list_filter = ("status",)
    search_fields = ['title','content']
    summernote_fields = ('content',)
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(Post,PostAdmin)
