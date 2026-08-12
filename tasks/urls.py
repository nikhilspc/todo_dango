from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    
    path('categories/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),
    
    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategory/add/', views.subcategory_add, name='subcategory_add'),
    path('subcategory/edit/<int:id>/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategory/delete/<int:id>/', views.subcategory_delete, name='subcategory_delete'),
]

