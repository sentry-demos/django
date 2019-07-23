from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.TextField(),
    count = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.count)
