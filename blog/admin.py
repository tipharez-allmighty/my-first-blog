from django.contrib import admin
from .models import Post, PostDocument, Comment

admin.site.register(Post)
admin.site.register(PostDocument)
admin.site.register(Comment)