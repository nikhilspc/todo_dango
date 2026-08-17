from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .models import Task, Category, SubCategory, Product
from .forms import (
    TaskForm,
    CategoryForm,
    SubCategoryForm,
    ProductForm
)

# HOME

@login_required(login_url='login')
def home(request):
    tasks = Task.objects.filter(
        user=request.user,
        is_deleted=False
    ).order_by('-id')

    return render(request, 'tasks/home.html', {
        'tasks': tasks
    })


@login_required(login_url='login')
def add_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')

    else:
        form = TaskForm()

    return render(request, 'tasks/form.html', {
        'form': form
    })


@login_required(login_url='login')
def edit_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/form.html', {
        'form': form
    })


@login_required(login_url='login')
def delete_task(request, id):

    task = get_object_or_404(
        Task,
        id=id,
        user=request.user
    )

    task.is_deleted = True
    task.save()

    return redirect('home')



# CATEGORY CRUD


@login_required(login_url='login')
def category_list(request):

    categories = Category.objects.all().order_by('-id')

    return render(request,
                  'tasks/category_list.html',
                  {'categories': categories})


@login_required(login_url='login')
def category_add(request):

    if request.method == "POST":

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category_list')

    else:
        form = CategoryForm()

    return render(request,
                  'tasks/category_form.html',
                  {'form': form})


@login_required(login_url='login')
def category_edit(request, id):

    category = get_object_or_404(Category, id=id)

    if request.method == "POST":

        form = CategoryForm(
            request.POST,
            instance=category
        )

        if form.is_valid():
            form.save()
            return redirect('category_list')

    else:
        form = CategoryForm(instance=category)

    return render(request,
                  'tasks/category_form.html',
                  {'form': form})


@login_required(login_url='login')
def category_delete(request, id):

    category = get_object_or_404(Category, id=id)
    category.delete()

    return redirect('category_list')


# SUBCATEGORY CRUD

@login_required(login_url='login')
def subcategory_list(request):

    subcategories = SubCategory.objects.all().order_by('-id')

    return render(request,
                  'tasks/subcategory_list.html',
                  {'subcategories': subcategories})


@login_required(login_url='login')
def subcategory_add(request):

    if request.method == "POST":

        form = SubCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('subcategory_list')

    else:
        form = SubCategoryForm()

    return render(request,
                  'tasks/subcategory_form.html',
                  {'form': form})


@login_required(login_url='login')
def subcategory_edit(request, id):

    subcategory = get_object_or_404(
        SubCategory,
        id=id
    )

    if request.method == "POST":

        form = SubCategoryForm(
            request.POST,
            instance=subcategory
        )

        if form.is_valid():
            form.save()
            return redirect('subcategory_list')

    else:
        form = SubCategoryForm(instance=subcategory)

    return render(request,
                  'tasks/subcategory_form.html',
                  {'form': form})


@login_required(login_url='login')
def subcategory_delete(request, id):

    subcategory = get_object_or_404(
        SubCategory,
        id=id
    )

    subcategory.delete()

    return redirect('subcategory_list')



# PRODUCT CRUD

@login_required(login_url='login')
def product_list(request):

    products = Product.objects.all().order_by('-id')

    return render(request,
                  'tasks/product_list.html',
                  {'products': products})


@login_required(login_url='login')
def product_add(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request,
                  'tasks/product_form.html',
                  {'form': form})


@login_required(login_url='login')
def product_edit(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    return render(request,
                  'tasks/product_form.html',
                  {'form': form})


@login_required(login_url='login')
def product_delete(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    product.delete()

    return redirect('product_list')


# REGISTER

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request,
                  'tasks/register.html',
                  {'form': form})


# LOGIN


def user_login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request,
                  'tasks/login.html',
                  {'form': form})


# LOGOUT


@login_required(login_url='login')
def user_logout(request):

    logout(request)

    return redirect('login')