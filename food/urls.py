from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list_view.as_view(), name='item_list'),
    path('add/', views.AddItemView.as_view(), name='add_item'),
    path('edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
]
