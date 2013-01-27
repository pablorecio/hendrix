from django.contrib import admin

from .models import Link, Tag


class LinkAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    fields = ("name", )


admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)
