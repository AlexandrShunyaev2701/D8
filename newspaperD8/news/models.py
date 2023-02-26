from django.db import models
from django.contrib.auth.models import User



    
class Post(models.Model):
    post = 'P'
    news = 'N'

    POSITIONS = [
        (post, 'Статья'),
        (news, 'Новость')
    ]
    author_news = models.ForeignKey('Author', on_delete=models.CASCADE)
    position = models.CharField(max_length=1, choices=POSITIONS, default=news)
    data_time_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')
    headline = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0.0)
    
    def like(self):
        self.rating += 1
        self.save()
        
    def dislike(self):
        self.rating -= 1
        self.save()
        
    def preview(self):
        return self.text[:124]
    
    def __str__(self):
        return f'{self.headline}'
        
    
class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    categorys = models.ForeignKey('Category', on_delete=models.CASCADE)
    
class Comment(models.Model):
    posts_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TimeField()
    comment_data_time = models.DateTimeField(auto_now_add=True)
    comments_rating = models.FloatField(default=0.0)
    
    def like(self):
        self.comments_rating += 1
        self.save()
        
    def dislike(self):
        self.comments_rating -= 1
        self.save()


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.FloatField(default=0.0)

    def update_rating(self):
        self.user_rating = self.Post.rating * 3 + self.Comment.comments_rating
        self.save()

class Category(models.Model):
    name_category = models.CharField(max_length=255, unique = True)


