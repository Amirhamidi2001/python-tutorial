from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)
    is_active = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
