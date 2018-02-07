from django.shortcuts import render, redirect
from django.http import HttpResponse
from dt_tdd.models import Item
# Create your views here.


def home_page(request):
    if request.method == "POST":
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/dt_tdd/the-only-list-in-the-world/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def view_list(requesst):
    items = Item.objects.all()
    return render(requesst, 'home.html', {'items': items})
