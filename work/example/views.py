from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
# Create your views here.
#Views that follow what is called CRUD (Create, Retrieve, Update and Delete)

def listing_list(request):
    listing = Listing.objects.all() #we can use .create, .update, .delete based on what you want to do
    context = {
        "listings": listing
    }
    return render(request, "listings.html", context) #context is a data we want to inject into this template. It is a python dictionary

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def listing_delete(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_delete.html", context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)