from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date", )
    list_display = ("title", "date", "author", )
    prepopulated_fields = {
        "slug" : ("title", ) #adding an extra comma beside an element enclosed within parantheses makes it a tuple. If the extra comma is not added, it is not treated as a tuple.
    }

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)