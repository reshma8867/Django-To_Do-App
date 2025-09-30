from django.urls import path
from base import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('about',views.about,name='about'),
    path('support',views.support,name='support'),
    path('history',views.history,name='history'),
    path('completed',views.completed,name='completed'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('restore_task/<int:pk>',views.restore_task,name='restore_task'),
    path('restore_all',views.restore_all,name='restore_all'),
    path('clear_all',views.clear_all,name='clear_all'),
    path('confirm_dalete/<int:pk>',views.confirm_delete,name='confirm_delete'),

    path('undo_complete/<int:id>/', views.undo_complete, name='undo_complete'),
    path('delete_completed/<int:id>/', views.delete_completed, name='delete_completed'),
    path('complete/<int:id>/', views.complete_task, name='complete'), 
    # urls.py
path('completed/', views.completed_tasks, name='completed'),

]

