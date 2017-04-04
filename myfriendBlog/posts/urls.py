from django.conf.urls import url
from django.contrib import admin
from posts.views import (post_detail,post_create,post_delete,post_update,index,about,contact
	,categories)
from django.conf.urls import include

import tinymce

urlpatterns = [
    url(r'^create',post_create),
    url(r'^update',post_update),
    url(r'^delete',post_delete),
    url(r'^(?P<id>\d+)/',post_detail), #you can mention here the post deatil specific page 
    url(r'^$',index),
    url(r'^about.html/$',about),
    url(r'^contact.html/$',contact),
    url(r'^categories.html/$',categories),
    url(r'^tinymce/', include('tinymce.urls')),


]