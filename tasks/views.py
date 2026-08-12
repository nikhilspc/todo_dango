from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .models import Task, Category, SubCategory, Product
from .forms import ProductForm

def home(request):
    tasks = Task.objects.filter(is_deleted=False).order_by('-id')
    return render(request, 'tasks/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'tasks/form.html', {'form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/form.html', {'form': form})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_deleted = True
    task.save()
    return redirect('home')

# ---------------- Category ----------------

from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all().order_by('-id')
    return render(request, 'tasks/category_list.html', {
        'categories': categories
    })


def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'tasks/category_form.html', {
        'form': form
    })


def category_edit(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'tasks/category_form.html', {
        'form': form
    })


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')

# ---------------- Sub Category ----------------

from .models import SubCategory
from .forms import SubCategoryForm


def subcategory_list(request):
    subcategories = SubCategory.objects.all().order_by('-id')
    return render(request, 'tasks/subcategory_list.html', {
        'subcategories': subcategories
    })


def subcategory_add(request):
    if request.method == "POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubCategoryForm()

    return render(request, 'tasks/subcategory_form.html', {
        'form': form
    })


def subcategory_edit(request, id):
    subcategory = get_object_or_404(SubCategory, id=id)

    if request.method == "POST":
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubCategoryForm(instance=subcategory)

    return render(request, 'tasks/subcategory_form.html', {
        'form': form
    })


def subcategory_delete(request, id):
    subcategory = get_object_or_404(SubCategory, id=id)
    subcategory.delete()
    return redirect('subcategory_list')

# ---------------- Product ----------------

def product_list(request):
    products = Product.objects.all().order_by('-id')

    return render(request, 'tasks/product_list.html', {
        'products': products
    })


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'tasks/product_form.html', {
        'form': form
    })


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    return render(request, 'tasks/product_form.html', {
        'form': form
    })


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()

    return redirect('product_list')