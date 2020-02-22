from django.db import models

# Create your models here.
class ProjectSubmission(models.Model):
    CHOICES = (
        ('1', '2 to 4 Weeks'),
        ('2', '4 to 6 Weeks'),
        ('3', '6 to 8 Weeks')
    )
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    title = models.CharField(max_length=2000)
    desc = models.TextField()
    duration = models.CharField(max_length=50, choices=CHOICES, default='2 to 4 Weeks')

    def __str__(self):
        return f"submission by {self.name}"
