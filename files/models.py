from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class File(models.Model):
    url = models.URLField(null=True)
    content = models.TextField()

    content_search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=["content_search_vector"])]

    def __repr__(self):
        return f"[{self.pk}] {self.url}"
