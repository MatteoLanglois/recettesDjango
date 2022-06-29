from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from .models import Recipe, Has_Ingredient, Ingredient, Tag, Has_Tags


def index(request):
    latest_recipes_list = Recipe.objects.order_by('-pub_date')[:5]
    recipes = Recipe.objects.all()
    has_t = Has_Tags.objects.all()
    context = {
        'latest_recipes_list': latest_recipes_list,
        'recipes': recipes,
        'has_t': has_t,
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


def OrderList(request, filter="title"):
    recipes = Recipe.objects.order_by(filter)
    has_t = Has_Tags.objects.all()
    context = {
        'recipes': recipes,
        'has_t': has_t,
    }
    return render(request, 'recettes/index.html', context)


def search(request):
    if 'search' in request.POST:
        q = request.POST['search']
        recipes = Recipe.objects.filter(title__icontains=q)
        has_t = Has_Tags.objects.all()
        context = {
            'recipes': recipes,
            'has_t': has_t,
        }
        return render(request, 'recettes/index.html', context)
    else:
        return render(request, 'recettes/index.html')

