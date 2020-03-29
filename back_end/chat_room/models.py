from django.db import models
import random
import string
from django.contrib.auth.models import User


def random_hash(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


class Room(models.Model):
    
    hash_id = models.CharField(max_length=8, blank=True, unique=True)
    creator = models.ForeignKey(User, verbose_name="creator", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="invited", related_name="invited")
    name = models.CharField(verbose_name="name", default="no_name", max_length=50)
    date = models.DateTimeField(verbose_name="date", auto_now_add=True)
    private = models.BooleanField(verbose_name="private", default=False)

    def save(self, *args, **kwargs):
        self.hash_id = random_hash(8)
        super().save(*args, **kwargs)

    def __str__ (self):
        return f'{self.name}'
