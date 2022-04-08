from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Rating(models.Model):
    design = models.IntegerField(blank=True)
    usability = models.IntegerField(blank=True)
    content = models.IntegerField(blank=True)
    ratings = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rate')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,related_name="rated")
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.ratings.username)
class Project(models.Model):
    name = models.CharField(max_length=100,blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    link = models.URLField(blank=True,max_length=200)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.project_name)

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='profile_username')
    description = models.TextField(blank=True)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.username.username)


