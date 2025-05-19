from django.urls import path
from .views import index, show, create, edit, update, delete, create_comment

app_name = 'article'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', show, name='show'),
    path('create/', create, name='create'),
    path('<int:pk>/edit/', edit, name='edit'),
    path('<int:pk>/update/', update, name='update'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/comments/', create_comment, name='create_comment')
]


