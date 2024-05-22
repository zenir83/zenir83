from django.shortcuts import render
from item.models import Category, Item

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[0:6] # too show items that are not sold on the frontpage and show the 6 newest items for sale
    categories = Category.objects.all()
    return render(request, 'core/index.html', 
    {'categories': categories,
     'items': items,
    
    })

def contact(request):
    return render(request, 'core/contact.html')

