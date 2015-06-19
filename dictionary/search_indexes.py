from haystack import indexes
from dictionary.models import Word


class WordIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    finnish = indexes.CharField(model_attr='finnish')

    def get_model(self):
        return Word

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
