"Models for storing snippet content."

from django.db import models


class Scribble(models.Model):
    "Core model for storing snippet content."

    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    modified_time = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255, blank=True, default=u"")
    slug = models.SlugField(max_length=255, blank=True, default=u"")
    url = models.CharField(max_length=255, blank=True, default=u"")
    content = models.TextField(blank=True, default=u"")
