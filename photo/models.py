
from django.db import models
from django.utils.text import slugify
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class tokomodel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # デフォルト値として1を指定

    def __str__(self):
        return self.title

