from django.urls import path
# Импортируем созданные нами представления
from .views import *

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:id>', OnePost.as_view()),
   path('search/', PostSearch.as_view()),
   path('news/create/', PostCreate.as_view()),
   path('articles/create/', NewsCreate.as_view()),
   path('news/<int:pk>/edit', PostEdit.as_view()),
   path('articles/<int:pk>/edit', NewsEdit.as_view(), name='post_list'),
   path('<int:pk>/delete', PostDelet.as_view()),
   path('upgrade/', upgrade_me, name = 'upgrade')

]
