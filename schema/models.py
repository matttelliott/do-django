from functools import partial
from django.db import models
from django.db.models.fields.files import ImageField
from datetime import datetime


def image_path(model: str, instance, filename: str) -> str:
    return "{timestamp}-{model}-{id}-{filename}".format(
        id=instance.id,
        filename=filename,
        model=model,
        timestamp=datetime.now().timestamp(),
    )


class Author(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    image = ImageField(null=True, blank=True, upload_to=partial(image_path, "author"))

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    body = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="articles",
    )
    image = ImageField(null=True, blank=True, upload_to=partial(image_path, "article"))

    def __str__(self):
        return self.title
