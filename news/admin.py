from django.contrib import admin
from .models import Comment, News, Images

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Images)
