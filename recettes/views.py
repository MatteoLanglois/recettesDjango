from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from .models import Recipe, Ingredient, Tag


def index(request):
    tri = "title"
    recipes = Recipe.objects.order_by(tri)
    if request.POST:
        if "filterDir" in request.POST:
            tri = request.POST["filterDir"]
            recipes = Recipe.objects.order_by(tri)
        if "filter" in request.POST:
            q = request.POST["filter"]
            recipes = Recipe.objects.filter(tag__name__iexact=q)
        elif "search" in request.POST:
            q = request.POST['search']
            recipes = Recipe.objects.filter(title__icontains=q).order_by(tri)
    context = {
        'recipes': recipes,
        'tags': Tag.objects.distinct().values_list('name', flat=True),
    }
    return render(request, 'recettes/index.html', context)


def detail(request, recette_id):
    recette = Recipe.objects.get(pk=recette_id)
    return render(request, 'recettes/detail.html', {
        'recette': recette,
    })

