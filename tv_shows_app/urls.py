from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('shows', views.index),
    path('<int:id>', views.show_info),
    path('new', views.new_show),
    path('add_show', views.add_show),
    path('<int:id>/edit', views.edit),
    path('delete/<int:id>', views.delete_show),
    path('edit_show/<int:id>', views.edit_show),
]