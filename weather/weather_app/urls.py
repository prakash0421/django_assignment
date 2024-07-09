from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('new_user/',views.user,name='user'),
    path('exist_user/',views.exist_user,name='exist_user'),
    path('delete/<int:user_id>',views.delete,name='delete')
]