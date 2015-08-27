from django.contrib import admin

# Register your models here.
from parts.models import Article, Brand, BrandAlias, Cross


class BrandInline(admin.StackedInline):
    model = BrandAlias
    fields = ['alias']
    extra = 2


class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [BrandInline]


class ArticleAdmin(admin.ModelAdmin):
    fields = ['brand', 'number', 'descr']
    list_filter = ['brand', 'number']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Cross)