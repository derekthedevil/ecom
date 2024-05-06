from django.urls import path




from product import views
urlpatterns = [
    path('add/', views.add_product),
    path('view/', views.view_products),
    path('edit_product/<int>', views.edit_product,),
    path('delete/<int>', views.delete),
]

