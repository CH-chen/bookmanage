from django.conf.urls import url
import views

urlpatterns=[
    url(r'^pub',views.publisher),
    # url(r'^add_pub/$',views.add_publisher),
    url(r'^add_pub/$',views.AddPub.as_view()),
    url(r'^test',views.test),
    url(r'^del/$',views.del_pub),
    url(r'^del2/([0-9]+)',views.del_pub2),
    url(r'^editor_pub',views.editor_pub),
    url(r'^book',views.book),
    url(r'^editor_book',views.editor_book),
    url(r'^author',views.author),
    url(r'^editor_author',views.editor_author),
]