from django.shortcuts import render, redirect
from .models import ProgrammingLanguage

def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'prog_platform_module/index.html')

def language_list(request):
    languages = ProgrammingLanguage.objects.all().order_by('name')
    return render(request, 'prog_platform_module/languageList.html', {'languages': languages})



def language_details(request, lang_id):

    language = ProgrammingLanguage.objects.get(id=lang_id)
    
    if language is None: return redirect('language_list')
    
    context = {'language': language} 
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



def add_language(request):
    if request.method == 'POST':
        name = request.POST['name']
        creator = request.POST['creator']
        release_year = request.POST['release_year']
        paradigm = request.POST['paradigm']
        typical_use = request.POST['typical_use']
        language = ProgrammingLanguage(name=name, creator=creator, release_year=release_year, paradigm=paradigm, typical_use=typical_use)
        language.save()
        return redirect('language_list')
    return render(request, 'prog_platform_module/add_language.html')

def update_language(request, lang_id):
    language = ProgrammingLanguage.objects.get(id=lang_id)
    if request.method == 'POST':
        language.name = request.POST['name']
        language.creator = request.POST['creator']
        language.release_year = request.POST['release_year']
        language.paradigm = request.POST['paradigm']
        language.typical_use = request.POST['typical_use']
        language.save()
        return redirect('language_details', lang_id=language.id)
    return render(request, 'prog_platform_module/update_language.html', {'language': language})
