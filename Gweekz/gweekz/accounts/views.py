from django.shortcuts import render
from .forms import ProductForm
from .models import Product

# Create your views here.


def checkout(request):
    context = {}
    return render(request, "accounts/checkout.html", context)


def games(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/games.html", context)


def home(request):
    context = {}
    return render(request, "accounts/home.html", context)


def login(request):
    context = {}
    return render(request, "accounts/login.html", context)


def register(request):
    context = {}
    return render(request, "accounts/register.html", context)

def profile(request):
    context = {}
    return render(request, "accounts/profile.html", context)



def upload(request):
    form = ProductForm()
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "accounts/upload.html", context)
