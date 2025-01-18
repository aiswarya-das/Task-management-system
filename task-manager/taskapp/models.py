from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.title
            + " "
            + self.description
            + " "
            + str(self.is_completed)
            + " "
            + str(self.created_at)
            + " "
            + str(self.updated_at)
        )
