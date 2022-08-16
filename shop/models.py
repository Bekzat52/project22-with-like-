from django.db import models
from rest_framework.viewsets import ModelViewSet, GenericViewSet 
from rest_framework import mixins
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length = 100)



class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='product')
    title = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    image = models.ImageField(upload_to = 'products', blank= True, null=True)
    
    @property
    def avarage_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
     
    

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)


