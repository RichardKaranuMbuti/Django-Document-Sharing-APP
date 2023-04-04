from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os

def upload_document(request):
    if request.method=='POST' and request.FILES['document']:
        document=request.FILES['document']
        fs=FileSystemStorage()
        filename=fs.save(document.name, document)
        uploaded_file_url=fs.url(filename)
        return render (request, 'documentmodule/upload_document.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'documentmodule/upload_document.html')


def download_document(request, filename):
    file_path=os.path.join(settings.MEDIA_ROOT,file_name)
    with open(file_path, 'rb') as f:
        response=HttpResponse(f.read(), content_type='application/force-download')
        response['Content-Disposition']='attachement; filename=' + os.path.basename(file_path)
        return response





