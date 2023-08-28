from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=200)
  author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
  image = models.ImageField(upload_to='post_images/', blank=True, null=True)
  body=models.TextField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('blog:detail',args=[str(self.id)])