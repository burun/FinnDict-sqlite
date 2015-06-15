from django.db import models
from django.template.defaultfilters import slugify


class Word(models.Model):
    finnish = models.CharField(max_length=128, unique=True)
    english = models.CharField(max_length=128)
    chinese = models.CharField(max_length=128, blank=True)
    sentence = models.CharField(max_length=256, blank=True)
    note = models.CharField(max_length=256, blank=True)
    category = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.finnish

    def save(self, *args, **kwargs):
        self.slug = slugify(self.finnish)
        super(Word, self).save(*args, **kwargs)
