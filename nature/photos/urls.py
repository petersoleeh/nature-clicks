from django.conf.urls import url
from . import views

urlpatterns=[
    #The landing page
    url(r'^$',views.index,name='index'),

    #The page to view a full size image and its details
    url(r'^(?P<post_id>[0-9]+)/$',views.single_image,name='image_details')
]
