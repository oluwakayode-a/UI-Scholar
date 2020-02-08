from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


User = get_user_model()

class University(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(University, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'universities'

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


class Level(models.Model):
    name = models.IntegerField()
    slug = models.SlugField(max_length=500, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Level, self).save(*args, **kwargs)



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
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    file_type = models.CharField(
        max_length=50, default='document', choices=CHOICES)

    def __str__(self):
        return self.name


class Review(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"
