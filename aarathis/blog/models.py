
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name



#create your models here
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
        content = models.TextField()


    



