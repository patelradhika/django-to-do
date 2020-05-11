from django.db import models

# Create your models here.
class Todolist(models.Model):
    item = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.item