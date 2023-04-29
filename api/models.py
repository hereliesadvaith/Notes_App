from django.db import models

# Create your models here.
# this is where we create our database


class Note(models.Model):
    # attributes works as columns and instances work as rows
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # returns the first 50 characters
        return self.body[0:50]
