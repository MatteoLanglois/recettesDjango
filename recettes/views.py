from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.utils import timezone
from .models import Recipe, Ingredient, Tag
from django.shortcuts import redirect

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
    if request.POST:
        r = get_object_or_404(Recipe, pk=recette_id)
        r.delete()
        return redirect('/recettes/')
    recette = Recipe.objects.get(pk=recette_id)
    return render(request, 'recettes/detail.html', {
        'recette': recette,
    })


def about(request):
    return render(request, 'recettes/about.html', {
        'recettes': Recipe.objects.all(),
    })


def add(request):
    if request.POST:
        ingredients = request.POST['ingredients'].split(',')
        tags = request.POST['tags'].split(',')
        r = Recipe.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            pub_date=timezone.now(),
        )
        r.ingredients.set(Ingredient.objects.create(name=I, recipes_id=r) for I in ingredients)
        r.tags.set(Tag.objects.create(name=T, icon="fa-solid fa-utensils", recipes_id=r) for T in tags)
        return redirect('/recettes/')
    return render(request, 'recettes/add.html', {
        'ingredients': Ingredient.objects.all(),
        'tags': Tag.objects.all(),
    })
