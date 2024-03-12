from django.shortcuts import render, redirect

def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'prog_platform_module/index.html')

def language_list(request):
    # this view returns a list of programming languages
    return render(request, 'prog_platform_module/languageList.html')

def language_details(request, lang_id):
    
    language1 = {'id': 1, 'name': 'Python', 'creator': 'Guido van Rossum'}
    language2 = {'id': 2, 'name': 'JavaScript', 'creator': 'Brendan Eich'}
    
    targetLanguage = None
    if language1['id'] == lang_id: targetLanguage = language1
    if language2['id'] == lang_id: targetLanguage = language2
    
    if targetLanguage is None: return redirect('language_list')
    
    context = {'language': targetLanguage} # 'language' is the variable name accessible by the template
    return render(request, 'prog_platform_module/languageDetails.html', context)
