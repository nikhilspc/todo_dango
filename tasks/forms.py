from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','is_completed']
        

from .models import Task, Category , SubCategory


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
from .models import SubCategory

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name']