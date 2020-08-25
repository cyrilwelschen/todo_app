from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('<int:todo_id>/priority', views.priority, name='prio'),
    path('<int:todo_id>/update/', views.update, name='update'),
    path('new', views.create, name='new_todo'),
]
