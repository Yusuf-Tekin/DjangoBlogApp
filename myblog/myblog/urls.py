
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexpage,name = "index"),
    path('posts/<int:postid>/',views.gotopost,name="postdetail"),
    

]
