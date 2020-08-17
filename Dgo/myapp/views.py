import json
import hashlib

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User

from myapp import models
from myapp.models import Article


# 获取token
def get_token(request):
    req = json.loads(request.body)
    uname = req["username"]
    upwd = req["password"]
    if request.method == "POST":
        try:
            tmppwd =User.objects.get(username=uname).password
            if upwd == tmppwd:
                md5 = hashlib.md5()
                #把密码变成一个长度固定的字符串
                md5.update(upwd.encode("utf-8"))
                return JsonResponse({"status":"BS.201","X-Token":md5.hexdigest()})
            else:
                return JsonResponse({"status":"BS.401","msg":"username or password may wrong."})

        except User.DoesNotExist:
            return JsonResponse({"status":"BS.500","msg":"username is not exist."})


# 认证动作
def user_auth(request):
    token = request.META.get('HTTP_X_TOKEN', b'')
    print(token)
    if token:
        if token == '5416d7cd6ef195a0f7622a9c56b55e83':
            return('auth_sucess')
        else:
            return('auth_fail')
    else:
        return('auth_fail')


def blog(request):
    # 第一种增加
    # models.Article.objects.create(title='标题四', category_id=1, body='内容四', user_id=1)

    # 第二种增加
    # obj = models.Article(title='标题二', category_id=1, body='内容二', user_id=1)
    # obj.save()

    # 第三种增加
    # obj = {'title':'标题三', 'category_id':'1', 'body':'内容三', 'user_id':'1'}
    # models.Article.objects.create(**obj)

    # 修改
    # xiugai = models.Article.objects.filter(title='标题一').update(title='标题一（已修改）')

    # 删除
    # shanchu = models.Article.objects.filter(id=3).delete()

    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'blog_index':blog_index,
    }
    return render(request, 'index.html', context)


# 新增文章接口
def add_article(request):
    auth_res = user_auth(request)
    if auth_res == 'auth_fail':
        return JsonResponse({"status":"BS.401","msg":"user auth failed."})
    else:
        if request.method == "POST":
            req = json.loads(request.body)
            print(req)
            key_flag = req.get("title") and req.get("category_id") and req.get("body") and req.get("user_id") and len(
                req) == 4
            # 判断请求体是否正确
            if key_flag:
                title = req["title"]
                category_id = req['category_id']
                body = req["body"]
                user_id = req['user_id']
                # title返回的是一个list
                title_exist = Article.objects.filter(title=title)
                # 判断是否存在同名title
                if len(title_exist) != 0:
                    return JsonResponse({"status": "BS.400", "msg": "title aleady exist,fail to publish."})

                '''插入数据'''
                obj = {
                    "title": title,
                    "category_id": category_id,
                    "body": body,
                    "user_id": user_id
                }
                models.Article.objects.create(**obj)
                return JsonResponse({"status": "BS.200", "msg": "publish article sucess."})
            else:
                return JsonResponse({"status": "BS.400", "message": "please check param."})


# 查询文章接口
        if request.method == "GET":
            articles = {}
            query_art = Article.objects.all()
            for wsh in query_art:
                articles[wsh.title] = wsh.body
            return JsonResponse({"status":"BS.200","all_titles":articles,"msg":"query articles sucess."})


# 修改文章接口
def modify_article(request, article_id):
    if request.method == "PUT":
        req = json.loads(request.body)
        try:
            key_flag = req.get("title") and req.get("category_id") and req.get("body") and req.get("user_id") and len(req)==4
            if key_flag:
                title = req["title"]
                category_id = req["category_id"]
                body = req["body"]
                user_id = req["user_id"]
                title_exist = Article.objects.filter(title=title)
                if len(title_exist) > 1:
                    return JsonResponse({"status":"BS.400","msg":"title aleady exist."})
                '''更新数据'''
                old_art = Article.objects.get(id=article_id)
                old_art.title = title
                old_art.category_id = category_id
                old_art.body = body
                old_art.user_id = user_id
                old_art.save()
                return JsonResponse({"status":"BS.200","msg":"modify article sucess."})
        except Article.DoesNotExist:
            return  JsonResponse({"status":"BS.300","msg":"article is not exists,fail to modify."})


# 删除文章接口
    if request.method == "DELETE":
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            return JsonResponse({"status":"BS.200","msg":"delete article sucess."})
        except Article.DoesNotExist:
            return JsonResponse({"status":"BS.300","msg":"article is not exists,fail to delete."})