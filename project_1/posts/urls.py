from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('',views.post_list, name="list"),
    path('new-post/',views.post_new, name="new-post"),
    path('<slug:slug>',views.post_page, name="page"),
]