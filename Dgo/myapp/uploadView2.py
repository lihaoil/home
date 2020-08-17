from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import UploadFileForm


def handle_upload_file(file):
    with open('/Project/Django/directory/%s' % file.name, 'wb+') as f:
        for chunk in file.chunk():
            f.write(chunk)


def uploadFile(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            #handle_upload_file(form.files['file'])
            return HttpResponse('upload success!')
    else:
        form = UploadFileForm()
    return render(request, 'uploadForm.html', {'form': form})