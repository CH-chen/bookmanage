# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *
from book01 import models


# Create your views here.
def publisher(request):
    publ= publisherInfo.objects.all().order_by('id')
    publ2 = publisherInfo.objects.all().filter(name='北京出版社').count()
    print(publ2)
    context={'publ':publ}
    return render(request,'publisher.html',context)
def add_publisher(request):
    #添加出版社，判断输入是否为空，并返回提示
    error_message = ''
    if request.method=='POST':
        pub_name=request.POST.get('add_pub')
        if pub_name:
            models.publisherInfo.objects.create(name=pub_name)
            return redirect('/pub/')
        else:
            error_message = '出版社名字不能为空'
    return render(request,'add_pub.html',{'error':error_message})

def del_pub(request):

    del_id = request.GET.get('id')
    if del_id:

        models.publisherInfo.objects.get(id=del_id).delete()

        return redirect('/pub/')
#URL分组匹配传参形式，删除出版社的函数
def del_pub2(request,del2):
    if del2:
        models.publisherInfo.objects.get(id=del2).delete()
        return redirect('/pub/')


def editor_pub(request):
    #模板中已隐藏方式获取id值，修改并提交
    if request.method=='POST':
        edi_id = request.POST.get('pub_id')

        pub_edi = publisherInfo.objects.get(id=edi_id)
        pub_edi.name = request.POST.get('pub_name')
        pub_edi.save()
        return redirect('/pub/')

    #以get方式获取地址栏中的id,判断是否为真，并返回数据
    edi_id = request.GET.get('id')
    if edi_id:
        pub_edi = publisherInfo.objects.get(id=edi_id)
        return render(request, 'editor.html', {'pub_edi':pub_edi})
    else:
        return HttpResponse('不存在')

def book(request):
    all_book = bookInfo.objects.all()
    context={'all_book':all_book}
    return render(request,'book.html', context)
def editor_book(request):
    if request.method == 'POST':
        book_id= request.POST.get('book_id')
        book_name= request.POST.get('book_name')
        publ_id = request.POST.get('publsh')
        book = models.bookInfo.objects.get(id=book_id)
        book.bookName=book_name
        book.publisher_id=publ_id
        book.save()
        return redirect('/book/')

    book_id = request.GET.get('id')
    edi_book = bookInfo.objects.get(id=book_id)
    publ = publisherInfo.objects.all()

    return render(request,'editorbook.html', {'edi_book':edi_book, 'publ':publ})

def author(request):
    author_obj = Author.objects.all()
    context={'author_obj':author_obj}
    return render(request,'author.html',context)

def editor_author(request):
    if request.method=='POST':
        author_id = request.POST.get('author_id')
        authorname=request.POST.get('authorname')
        # post提交的是多个值的时候要用getlist,如多选的select,多选的checkbox
        new_book = request.POST.getlist('books')
        author=Author.objects.get(id=author_id)
        author.aname=authorname
        # 把当前作者关联的书设置成new_book
        author.book.set(new_book)
        author.save()
        return redirect('/author/')
    # 获取地址栏的id并显示当前的作者名和作者的书
    author_id = request.GET.get('id')
    author_obj = Author.objects.get(id=author_id)
    all_book = bookInfo.objects.all()
    context={'author_obj':author_obj,'allbook':all_book}

    return render(request,'editor_author.html', context)

#CBV(class base views,通过类添加出版社
from django.views import View

class AddPub(View):
    def get(self,request):
        return render(request, 'add_pub.html')
    def post(self,request):
        if request.method == 'POST':
            pub_name = request.POST.get('add_pub')
            if pub_name:
                models.publisherInfo.objects.create(name=pub_name)
                return redirect('/pub/')
            else:
                error_message = '出版社名字不能为空'
                return render(request, 'add_pub.html', {'error': error_message})


def test(request):
    print(request.GET)


    return HttpResponse('OK')


