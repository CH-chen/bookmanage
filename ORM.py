# -*- coding: utf-8 -*-

#如何在一个python脚本或文件中 加载Django项目的配置和变量信息
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanage.settings")
    import django
    django.setup()


    from book01 import models

    books = models.bookInfo.objects.all()
    print(books)
    book_obj = models.bookInfo.objects.all().first()
    ret = book_obj.publisher
    ret_name = book_obj.publisher.name
    print (ret)
    print(ret_name)