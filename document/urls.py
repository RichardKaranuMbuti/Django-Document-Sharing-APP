
from django.contrib import admin
from django.urls import path,include
from documentmodule import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/',views.upload_document, name='upload_document'),
    path('download/<str:file_name>/', views.download_document, name='download_document'),
    path('',include('documentmodule.urls'))
    

]
