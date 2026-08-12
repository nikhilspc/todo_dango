from django import forms
from .models import Task, Category, SubCategory, Product

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'subcategory',
            'name',
            'description',
            'price',
            'image'
        ]