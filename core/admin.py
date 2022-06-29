from django.contrib import admin
from django.db.models import Q
from .models import Post, Thread, ChatMessage

admin.site.register(Post)

admin.site.register(ChatMessage)


class ChatMessage(admin.TabularInline):
    model = ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)