from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PostModel(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post', validators=[
                              FileExtensionValidator(['png', 'jpg'])])

    class Meta:
        ordering = ('-date_created',)    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
