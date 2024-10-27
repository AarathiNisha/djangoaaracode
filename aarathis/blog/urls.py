from django.urls import path
from . import views

app_name= 'blog'
urlpatterns=[
    path('', views.index, name='index' ),
    path("post/<int:post_id>", views.detail, name="detail"),

    #Here first path("new_url we gave then we change according to us.So we need to enter old_url then the 
    # new_url will change to new_something_url")
    path("new_something_url", views.new_url_view, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("contact/", views.contact_view, name="contact"),
    path("about/", views.about_view, name="about"),
    
]
