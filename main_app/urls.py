from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('finch_index/', views.finch_index, name='finch-index'),
]
