from django.contrib import admin
from .models import ProductList,RecipeList,Quantities 



#Specifying how to show the Many to many field through our custom "through" table. 

class QuantitiesInline(admin.TabularInline):
    model=Quantities
    extra=0  #how many suggested addition,the default is 3 but i thought it did not look nice 



#adding the previous class to the inlines list
    
class RecipeListAdmin(admin.ModelAdmin):
    inlines = [QuantitiesInline]
    class Meta : 
        model=RecipeList


admin.site.register(RecipeList,RecipeListAdmin)
admin.site.register(ProductList)