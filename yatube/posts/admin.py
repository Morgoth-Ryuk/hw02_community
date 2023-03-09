from django.contrib import admin


from .models import Post
from .models import Group


class PostAdmin(admin.ModelAdmin):
    '''
    Регистрация и настройка отображения модели Post в админке.
    '''
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
