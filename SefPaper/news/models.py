from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRate = models.SmallIntegerField(default=0)

    def update_rating(self):
        for self
        pass


class Category(models.Model):
    CategoryName = models.CharField(max_length=128, unique=True)
    pass


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICED = (
        (NEWS, 'Новость')
        (ARTICLE, 'Статья')
    )

    typePost = models.CharField(max_length=2, choices=CATEGORY_CHOICED)
    daterimePost = models.DateTimeField(auto_now=True)
    categoryPost = models.ManyToManyField(Category, through='categoryPost')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislige(self):
        self.rating -= 1
        self.save()

    def prewiew(self):
        self.text[0:123] + '. . .' + str(self.rating)

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    pass


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    commentDate = models.DateTimeField(auto_now_add=True)
    commentRate = models.SmallIntegerField(default=0)

    def like(self):
        self.commentRate += 1
        self.save()

    def dislige(self):
        self.commentRate -= 1
        self.save()
