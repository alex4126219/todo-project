from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate,TaskUpdate, TaskDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/create/', TaskCreate.as_view(), name='task-create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(),name='task-delete'),
]