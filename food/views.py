from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def item_list(request):
    items = Food.objects.all()
    return render(request, 'food/item_list.html', {'items': items})

class item_list_view(ListView):
    model = Food
    template_name = 'food/item_list.html'
    context_object_name = 'items'

def add_item(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'food/add_item.html', {'form': form})

class AddItemView(CreateView):
    model = Food
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    template_name = 'food/add_item.html'

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