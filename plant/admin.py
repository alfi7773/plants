from django.contrib import admin

from django.utils.safestring import mark_safe
from .models import *

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Description)
admin.site.register(Blog)
admin.site.register(Cart)
admin.site.register(CartItem)


class PLntImageStackedInline(admin.TabularInline):

    model = ImagePlant
    extra = 1



@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'get_image')
    list_display_links = ('id', 'name',)
    list_filter = ('category','tags', 'user', 'sizes',)
    search_fields = ('name', 'description', 'sizes',)
    readonly_fields = ('created_at', 'updated_at', 'get_big_image',)
    inlines = [PLntImageStackedInline, ]

    @admin.display(description='Image')
    def get_image(self, item):
        if item.image:
            return mark_safe(f'<img src="{item.image.url}" width="150px">')
        return '-'

    @admin.display(description='Image')
    def get_big_image(self, item):
        if item.image:
            return mark_safe(f'<img src="{item.image.url}" width="100%">')
        return '-'


# Register your models here.
