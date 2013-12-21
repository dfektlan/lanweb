from django.contrib import admin
from apps.news.models import Post

class PostAdmin(admin.ModelAdmin):
# fields display on change list
    list_display = ['title', 'summary', 'author', 'event']
# fields to filter the change list with
    list_filter = ['created']
# fields to search in change list
    search_fields = ['title', 'summary', 'content']
# enable the date drill down on change list
    date_hierarchy = 'created'
# enable the save buttons on top on change form
    save_on_top = True
# prepopulate the slug from the title - big timesaver!
#    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
