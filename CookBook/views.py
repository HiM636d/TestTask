from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductList,RecipeList,Quantities 
from django.db import transaction 
from django.db.models import F

def Add_product_to_recipe(request):
    product_id=request.GET.get('product_id')
    recipe_id=request.GET.get('recipe_id')
    quantity=request.GET.get('quantity_in_grams')
    with transaction.atomic(): 
        Quantities.objects.update_or_create(products_id=product_id,recipe_id=recipe_id,defaults= { "quantity_in_grams" : quantity})




def Cook_recipe(request): 
    with transaction.atomic():      
        recipe_id=request.GET.get('recipe_id')
        Cooked= RecipeList.objects.get(id=recipe_id)
        Cooked.amount_cooked = F('amount_cooked') + 1  #The F class instructs the database to increment the field without pulling it, avoiding race condition
        Cooked.save()





def show_recipe_without_product(request):
    product_id_para=request.GET.get('product_id')
    
    #filtering to get recipes that contain product, and the where amount is greater or equal than 10grams
    #then getting a list of ids of recipes and by assigning flat to true i avoid getting back a list of tuples
    #the whole queryset is wrapped in list() so the end result is a list of ids of recipes containing product gte to 10
    recipes_containing_product=list(Quantities.objects.filter(products_id=product_id_para,quantity_in_grams__gte=10).values_list('recipe_id', flat=True))
    
    #getting recipes excluding the recipes that contain product
    recipes_not_containing=RecipeList.objects.exclude(id__in=recipes_containing_product)
    
    #returning an html and passing it the list of recipes that do not contain product
    return render(request,'recipes_without_product.html',{'list_of_recipes' :recipes_not_containing})
