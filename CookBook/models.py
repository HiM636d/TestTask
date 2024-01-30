from django.db import models

#Products or ingredients 

class ProductList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


#Recipes, the through parameter is used because 
#standard ManyToMany field does not attach any information to the relationship,and we need to add quantity
    
class RecipeList(models.Model):
    name= models.CharField(max_length=100)
    products = models.ManyToManyField(ProductList , through = 'Quantities')
    amount_cooked = models.IntegerField()

    def __str__(self):
        return self.name
    



#custom "through" table,usually Django creates its own through table behind the scenes,
#i had to override it so i can pass some information (the quantity) with it
    
class Quantities(models.Model):
    products = models.ForeignKey(ProductList , on_delete=models.CASCADE)   
    recipe = models.ForeignKey(RecipeList ,on_delete=models.CASCADE)
    quantity_in_grams = models.IntegerField(default=1)

    class Meta:
        unique_together=['products','recipe']
