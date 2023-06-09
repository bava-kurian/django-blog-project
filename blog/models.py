from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here. 
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text=models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)
    published_date=models.DateField(blank=True,null=True)
    
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def approve_comment(self):
        return self.comments.filters(approve_comment=True)
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    def __str__(self) :
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=255)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approve_comments=models.BooleanField(default=False)
    
    def approve(self):
        self.approve_comment=True
    def get_absolute_url(self):
        return reverse("post_list")
    def __str__(self):
        return self.text
    
    