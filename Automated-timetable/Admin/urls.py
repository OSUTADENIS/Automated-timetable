from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('add_stuff',add_stuff, name='add_stuff'),

    path('delete_stuff/<int:myid>',delete_stuff, name='delete_stuff'),

    path('edit_stuff/<int:myid>',edit_stuff, name='edit_stuff'),

    path('update_stuff/<int:myid>',update_stuff, name='update_stuff'),


]