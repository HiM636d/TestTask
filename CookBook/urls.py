from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_recipe_without_product)

]   