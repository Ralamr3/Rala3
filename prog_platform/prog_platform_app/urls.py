from django.urls import path, re_path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('languages', views.language_list),
    path('filter_language',views.filter_language,name="filter_language"),
    path('add_language',views.add_language,name="add_language"),
    path('language/<int:lang_id>', views.language_details,name='language_details'),
    path('update_language/<int:lang_id>',views.update_language,name="update_language")
]