from django.shortcuts import render
from dictionary.models import Word


def index(request):
    context_dict = {}
    return render(request, 'dictionary/index.html', context_dict)


def list(request):
        # Get the sorted vocabulary.
    words_list = Word.objects.extra(
        select={'case_insensitive_finnish': 'lower(finnish)'}).order_by('case_insensitive_finnish')
    context_dict = {'words_list': words_list}
    return render(request, 'dictionary/list.html', context_dict)


def word(request, word_name_slug):
    context_dict = {}

    try:
        word = Word.objects.get(slug=word_name_slug)
        context_dict['word_finnish'] = word.finnish
        context_dict['word_english'] = word.english
        context_dict['word_chinese'] = word.chinese
        context_dict['word_name_url'] = word_name_slug
    except Word.DoesNotExist:
        pass

    return render(request, 'dictionary/word.html', context_dict)
