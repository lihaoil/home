from django.db import models
from django import forms
from django.contrib.auth.models import User

# 练习
class Category(models.Model):
    name = models.CharField('分类', max_length=100)

    class Meta:
        # 指定model对应数据库表名
        db_table = 'Category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField('标签', max_length=100)

    class Meta:
        db_table = 'Tags'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    intro = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', default='1')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='标签')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 文件上传
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()