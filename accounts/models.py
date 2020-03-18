from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

BaseUser = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    profile_pic = models.ImageField(blank=True)
    desc = models.CharField(max_length=1000, blank=True)
    bio = models.TextField(blank=True)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return f"{self.id}/profile/"


@receiver(post_save, sender=BaseUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=BaseUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
