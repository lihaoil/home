from django.shortcuts import render
from django.http import HttpResponse


def upload(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("no files for upload!")
        else:
            # 打开特定的文件进行二进制的写操作;
            with open("/Project/Django/directory/%s" % File.name, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("upload over!")
    else:
        return render(request, 'upload.html')