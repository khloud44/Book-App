from django.db import models


# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    image = models.FileField(upload_to='minBooks/static/minBooks/images/')
    price = models.IntegerField()
    published_at = models.DateField()
    add_to_site_at = models.DateTimeField(auto_now_add=True)
    appropriate_to = models.CharField(max_length=10, choices=[("-8", "Under 8"), ("+8", "8-15"), ("+15", "Adults")])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name