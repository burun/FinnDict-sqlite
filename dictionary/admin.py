from django.contrib import admin

from dictionary.models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('finnish', 'english', 'chinese')
    prepopulated_fields = {'slug': ('finnish',)}

admin.site.register(Word, WordAdmin)
