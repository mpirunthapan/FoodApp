from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm

def item_list(request):
    items = Food.objects.all()
    return render(request, 'food/item_list.html', {'items': items})

def add_item(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'food/add_item.html', {'form': form})

def edit_item(request, pk):
    item = get_object_or_404(Food, pk=pk)
    form = FoodForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'food/edit_item.html', {'form': form, 'item': item})

def delete_item(request, pk):
    item = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'food/delete_item.html', {'item': item})