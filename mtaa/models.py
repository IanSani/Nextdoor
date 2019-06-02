from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Hood(models.Model):
    hood_photo = models.ImageField(upload_to='hoods/')
    hood_name = models.CharField(max_length=100, null=True)
    occupants_count = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_hoods(cls):
        hoods = Hood.objects.all()
        return hoods

    @classmethod
    def search_hood(cls,hood_search):
        hoods = cls.objects.filter(id__icontains = hood_search)
        return hoods

    class Meta:
        ordering = ['hood_name']

class Business(models.Model):
    b_photo = models.ImageField(upload_to='business/',null=True)
    b_name = models.CharField(max_length=100, blank=True, null=True)
    b_description = models.TextField(max_length=200, blank=True, null=True)
    b_email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='biz',null=True)

    @classmethod
    def get_business(cls):
        business = Business.objects.all()
        return business

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo= models.ImageField(upload_to='profiles/',null=True)
    bio= models.CharField(max_length=240, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    class Meta:
        ordering = ['user']

class Join(models.Model):
	user_id = models.OneToOneField(User)
	hood_id = models.ForeignKey(Hood)

	def __str__(self):
		return self.user_id

class Posts(models.Model):
	title = models.CharField(max_length = 300)
	content = models.TextField()
	posted_by = models.ForeignKey(User, null=True)
	hood = models.ForeignKey(Hood)

	def save_posts(self):
		self.save()

	def delete_posts(self):
		self.delete()

	def __str__(self):
		return self.title
