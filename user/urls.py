from django.urls import path
from .views import index, add_and_edit

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_and_edit, name='add'),
    path('edit/<int:pk>/', add_and_edit, name='edit'),

]
