
from django.contrib import admin
from django.urls import path
from app.views import show_task, home, delete_task, create_task, update_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks', show_task, name = 'tasks'),
    path('delete/<int:task_id>', delete_task, name = 'delete'),
    path('create/', create_task, name = 'create'),
    path('update/<int:task_id>', update_task, name = 'update')
]
