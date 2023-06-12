from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='finch-index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail')
]
