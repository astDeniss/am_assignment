from django.db import models
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='category_obj')
    children = models.ManyToManyField(Category)

    def __str__(self):
        return self.category.name

    def create_profile(sender, **kwargs):
        category = kwargs["instance"]
        if kwargs["created"]:
            category_profile = Categories(category=category)
            category_profile.save()

    post_save.connect(create_profile, sender=Category)
