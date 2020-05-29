from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    path( '', views.index, name="index" ),
    path( 'partner', views.partner, name="partner" ),
    path( 'lecturer', views.lecturer, name="lecturer" ),
    path( 'upload', views.upload, name="upload" ),
    path( 'lectures', views.lectures, name="lectures" ),
    path( 'like', views.like, name='like' ),
    path( 'view/<int:id>', views.view, name='view' ),
    path( '<int:id>/details', views.details, name='details' )

]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
