from django.contrib import admin

from .models import Recipe, Ingredient, Has_Ingredient, Tag, Has_Tag


class Has_IngredientInline(admin.TabularInline):
    model = Has_Ingredient
    extra = 1


class Has_TagAdmin(admin.TabularInline):
    model = Has_Tag
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
    inlines = [Has_IngredientInline, Has_TagAdmin]


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measure')
    search_fields = ['name']
    empty_value_display = '-empty-'
    fieldsets = [
        (None, {'fields': ['name', 'measure']}),
    ]


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    empty_value_display = '-empty-'
    fieldsets = [
        (None, {'fields': ['name']}),
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(Has_Ingredient)
admin.site.register(Has_Tag)

