from django.shortcuts import render, redirect

def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'prog_platform_module/index.html')

def language_list(request):
    # this view returns a list of programming languages
    return render(request, 'prog_platform_module/languageList.html',{'languages':__getLanguages()})
def language_details(request, lang_id):
    
    language1 = {'id': 1, 'name': 'Python', 'creator': 'Guido van Rossum'}
    language2 = {'id': 2, 'name': 'JavaScript', 'creator': 'Brendan Eich'}
    
    targetLanguage = None
    if language1['id'] == lang_id: targetLanguage = language1
    if language2['id'] == lang_id: targetLanguage = language2
    
    if targetLanguage is None: return redirect('language_list')
    
    context = {'language': targetLanguage} # 'language' is the variable name accessible by the template
    return render(request, 'prog_platform_module/languageDetails.html', context)

def __getLanguages():
    return [
        {'id': 1, 'name': 'Python', 'creator': 'Guido van Rossum', 'release_year': 1991, 'paradigm': 'Object-oriented, Imperative, Functional', 'typical_use': 'Web development, Data Science, Automation'},
        {'id': 2, 'name': 'JavaScript', 'creator': 'Brendan Eich', 'release_year': 1995, 'paradigm': 'Event-driven, Functional', 'typical_use': 'Web development, Front-end scripting'},
        {'id': 3, 'name': 'Java', 'creator': 'James Gosling', 'release_year': 1995, 'paradigm': 'Object-oriented', 'typical_use': 'Enterprise applications, Android apps'},
        {'id': 4, 'name': 'C#', 'creator': 'Microsoft', 'release_year': 2000, 'paradigm': 'Object-oriented', 'typical_use': 'Desktop applications, Game development'},
        {'id': 5, 'name': 'Ruby', 'creator': 'Yukihiro Matsumoto', 'release_year': 1995, 'paradigm': 'Object-oriented', 'typical_use': 'Web applications, Scripting'}
    ]

def filter_language(request):
    all_languages = __getLanguages()
    search_name = request.GET.get('search_name', '')
    search_paradigm = request.GET.get('paradigm', '')

    if search_name:
        all_languages = [lang for lang in all_languages if search_name.lower() in lang['name'].lower()]
    if search_paradigm:
        all_languages = [lang for lang in all_languages if search_paradigm in lang['paradigm']]

    context = {'languages': all_languages}
    return render(request, 'prog_platform_module/languageList.html', context)