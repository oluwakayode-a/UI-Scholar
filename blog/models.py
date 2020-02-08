from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/category/{self.slug}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "categories"



class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=5000, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f"/post/{self.slug}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    email = models.EmailField()
    body = models.TextField()
    
    def __str__(self):
        return f"comment by {self.name} on {self.post}"
