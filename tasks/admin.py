from django.contrib import admin
from .models import Task, Category, SubCategory, Product

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)