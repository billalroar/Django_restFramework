from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class PostsRates(models.Model):
    likes = models.BigIntegerField(default=0)
    dislike = models.BigIntegerField(default=0)

class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField(max_length=1000)
    rates = models.OneToOneField(PostsRates, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.post_title
    

