import uuid
from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d/")
    phone = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    address = models.TextField()
    time = models.TimeField()
    web = models.URLField()
    uuid = models.UUIDField(default=uuid.uuid4)
    slug = models.SlugField()
    is_active = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
