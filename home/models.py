from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    image = models.ImageField(upload_to='post', validators=[
                              FileExtensionValidator(['png', 'jpg'])])
    
    def __str__(self):
        return self.title

class AboutFeatureCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class AboutStaff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post', validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name


class Choose(models.Model):
    name = models.ForeignKey(AboutFeatureCategory, on_delete=models.CASCADE)
    description = models.TextField()


class Service(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    

    def __str__(self):
        return self.title

class WorkProcess(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()

    class Meta:
        ordering = ('id',) 

    def __str__(self):
        return self.title 


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='post', validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name
