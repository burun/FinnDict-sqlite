from django.conf.urls import patterns, url
from dictionary import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^list/$', views.list, name='list'),
                       url(r'^word/(?P<word_name_slug>[\w\-]+)/$', views.word, name='word'),
                       url(r'^flashcard/$', views.flashcard, name='flashcard'),
                       )
