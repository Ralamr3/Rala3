from django.urls import path, re_path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('languages', views.language_list),
    path('language/<int:lId>', views.language_details)
]