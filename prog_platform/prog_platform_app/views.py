from django.shortcuts import render, redirect

from .forms import LanguageForm
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
        form = LanguageForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('language_details', lang_id=obj.id)
    else:
        form = LanguageForm()
    return render(request, 'prog_platform_module/add_language.html', {'form': form})

def update_language(request, lang_id):
    language = ProgrammingLanguage.objects.get(id=lang_id)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('language_details', lang_id=language.id)
    else:
        form = LanguageForm(instance=language)
    return render(request, 'prog_platform_module/update_language.html', {'form': form})


def delete_language(request, lang_id):
    language = ProgrammingLanguage.objects.get(id=lang_id)
    language.delete()
    return redirect('language_list')  # Redirect to the list of languages
