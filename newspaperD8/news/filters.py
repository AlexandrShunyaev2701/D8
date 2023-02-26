from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'headline': ['icontains'],
            'author_news': ['exact'],
            'data_time_create': ['lt'],
            'text': [],
        }