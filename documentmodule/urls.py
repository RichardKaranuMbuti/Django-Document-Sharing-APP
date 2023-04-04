from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.upload_document, name='upload_document'),
    path('download/<str:file_name>/', views.download_document, name='download_document'),

]