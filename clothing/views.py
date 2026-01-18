from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# Create your views here.
def home(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm()

    prod = Product.objects.all()
    return render(request, "clothing/home.html", {"prod": prod, "form": form})

def update_data(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        fm = ProductForm(request.POST, instance=product)
        if fm.is_valid():
            fm.save()
            return redirect("home")
    else:
        fm = ProductForm(instance=product)

    return render(request, "clothing/update.html", {"form": fm})

def delete_data(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect("home")