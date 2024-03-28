from django.shortcuts import render, redirect
from .models import ProgrammingLanguage

def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'prog_platform_module/index.html')

def language_list(request):
    languages = ProgrammingLanguage.objects.all().order_by('name')
    return render(request, 'prog_platform_module/languageList.html', {'languages': languages})



def language_details(request, lang_id):
    
    language1 = {'id': 1, 'name': 'Python', 'creator': 'Guido van Rossum'}
    language2 = {'id': 2, 'name': 'JavaScript', 'creator': 'Brendan Eich'}
    
    targetLanguage = None
    if language1['id'] == lang_id: targetLanguage = language1
    if language2['id'] == lang_id: targetLanguage = language2
    
    if targetLanguage is None: return redirect('language_list')
    
    context = {'language': targetLanguage} # 'language' is the variable name accessible by the template
    return render(request, 'prog_platform_module/languageDetails.html', context)


def filter_language(request):
    search_name = request.GET.get('search_name', '')
    search_paradigm = request.GET.get('paradigm', '')

    languages = ProgrammingLanguage.objects.all()
    if search_name:
        languages = languages.filter(name__icontains=search_name)
    if search_paradigm:
        languages = languages.filter(paradigm__icontains=search_paradigm)

    languages = languages.order_by('name')
    return render(request, 'prog_platform_module/languageList.html', {'languages': languages})