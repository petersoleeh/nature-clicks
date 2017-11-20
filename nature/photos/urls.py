from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #The landing page
    url(r'^$',views.index,name='index'),

    #The page to view a full size image and its details
    url(r'^(?P<post_id>[0-9]+)/$',views.single_image,name='image_details'),

    #contacts page
    url(r'^contacts/$',views.contacts,name='contacts'),

    #search posts
    url(r'^search/',views.search_results, name='search_results')

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
