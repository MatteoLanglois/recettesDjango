from django.contrib import admin

from .models import Recipe, Ingredient, Tag


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class TagAdmin(admin.TabularInline):
    model = Tag
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    empty_value_display = '-empty-'
    ordering = ['-pub_date']
    date_hierarchy = 'pub_date'
    fieldsets = [
        ('Recette', {'fields': ['title', 'description']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [IngredientInline, TagAdmin]


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measure', 'quantity')
    search_fields = ['name']
    empty_value_display = '-empty-'
    fieldsets = [
        (None, {'fields': ['name', 'measure', 'quantity']}),
    ]


class TagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']
    empty_value_display = '-empty-'
    fieldsets = [
        (None, {'fields': ['name', 'icon']}),
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagsAdmin)

