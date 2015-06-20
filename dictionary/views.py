from django.shortcuts import render, get_object_or_404
from dictionary.models import Word
from django.template import RequestContext


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


def flashcard(request):
    '''
    Practice the word by flashcard
    '''
    # Get all the words in database
    practices = Word.objects.order_by('times_practiced')
    practice = practices[0]
    context_dict = {'practice': practice}

    # Set next practiced word
    practice_word = get_object_or_404(Word, pk=int(practice.id))
    practice_word.set_next_practice()
    practice_word.save()

    return render(request, 'dictionary/flashcard.html', context_dict, context_instance=RequestContext(request))
