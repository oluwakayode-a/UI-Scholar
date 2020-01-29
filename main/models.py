from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


User = get_user_model()


class Level(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Level, self).save(*args, **kwargs)


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'faculties'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Faculty, self).save(*args, **kwargs)


class Department(models.Model):
    name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)


class Material(models.Model):
    CHOICES = [
        ('document', 'Document'),
        ('powerpoint', 'PowerPoint'),
        ('video', 'Video')
    ]

    name = models.CharField(max_length=500)
    file_path = models.FileField(blank=True)
    added_by = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    file_type = models.CharField(
        max_length=50, default='document', choices=CHOICES)

    def __str__(self):
        return self.name
