from django.db import models

# Create your models here.
class Post(models.Model):
    title = models. CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]--{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'