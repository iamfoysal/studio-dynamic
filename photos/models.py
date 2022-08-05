from django.db import models




# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null = False, blank =False)

    def __str__(self):
        return self.name
class Photo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    # title = models.CharField(max_length=50)
    description= models.TextField(max_length=255, null = False, blank =False)
    posted_at= models.DateTimeField(auto_now_add=True, null=True, blank=True)

    
    def __str__(self):
        return self.description
     

        