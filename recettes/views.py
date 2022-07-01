from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from .models import Recipe, Has_Ingredient, Ingredient, Tag, Has_Tag


def index(request):
    tri = "title"
    recipes = Recipe.objects.order_by(tri)
    if request.POST:
        if "filterDir" in request.POST:
            tri = request.POST["filterDir"]
            recipes = Recipe.objects.order_by(tri)
        if "filter" in request.POST:
            q = request.POST['filter']
            recipes = Recipe.objects.filter(has_label__tag__name__icontains=q).order_by(tri)
        elif "search" in request.POST:
            q = request.POST['search']
            recipes = Recipe.objects.filter(title__icontains=q).order_by(tri)

    context = {
        'recipes': recipes,
        'has_t': Has_Tag.objects.filter(),
        'tags': Tag.objects.all(),
    }
    return render(request, 'recettes/index.html', context)


def detail(request, recette_id):
    recette = Recipe.objects.get(pk=recette_id)
    ing = Ingredient.objects.filter(has_ingredient__kitchen=recette_id)
    has_ingredients = Has_Ingredient.objects.filter(kitchen=recette_id)
    ingredient = list(zip([ingr.quantity for ingr in has_ingredients],
                          [ingr.measure if ingr.measure != "nb" else "" for ingr in ing],
                          [ingr.name for ingr in ing],
                          ))
    return render(request, 'recettes/detail.html', {
        'recette': recette,
        'ing': ingredient,
    })

