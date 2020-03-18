from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/blog/category/{self.slug}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "categories"



class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=5000, blank=True)
    body = RichTextUploadingField()
    desc = models.CharField(max_length=1000)
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
        return f"/blog/post/{self.slug}"
    
    @property
    def number_of_comments(self):
        return self.comment_set.all().count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"comment by {self.user.username} on {self.post}"

