from django.urls import path
from . import views

urlpatterns = [
    path('addtask/',views.addTask,name='addTask'),                                   # to add task
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),          # to mark as done
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name ='mark_as_undone'),   # to mark us undone
    path('edit/<int:pk>/',views.edit,name='edit'),                                   # to edit task
    path('delete/<int:pk>/',views.delete,name='delete'), 
]