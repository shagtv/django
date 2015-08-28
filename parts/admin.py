from django.contrib import admin
from parts.models import Article, Brand, BrandAlias, Cross


class BrandInline(admin.StackedInline):
    model = BrandAlias
    fields = ['alias']
    extra = 2


class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [BrandInline]
    list_select_related = True
    search_fields = ['name_fix']
    list_per_page = 30
    ordering = ['-name_fix']


class ArticleAdmin(admin.ModelAdmin):
    fields = ['brand', 'number', 'descr']
    list_select_related = True
    search_fields = ['number_fix', 'brand__name_fix']
    raw_id_fields = ["brand"]
    list_per_page = 30


class CrossAdmin(admin.ModelAdmin):
    list_select_related = True
    raw_id_fields = ["article", "carticle"]
    search_fields = ['article__number_fix', 'article__brand__name_fix', 'carticle__number_fix', 'carticle__brand__name_fix']
    list_per_page = 30


admin.site.register(Article, ArticleAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Cross, CrossAdmin)