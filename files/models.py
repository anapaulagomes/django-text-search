from django.db import models


class File(models.Model):
    url = models.URLField(null=True)
    content = models.TextField()

    def __repr__(self):
        return f"[{self.pk}] {self.url}"
