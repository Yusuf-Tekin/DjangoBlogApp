from django.shortcuts import render
from django.contrib import messages
from .models import Posts,Admin

def indexpage(request):

    posts_data = Posts.objects.all().order_by('postdata').reverse()
    

    if len(posts_data) == 0:
        messages.error(request, 'Yayımlanmış veri bulunamadı.')

        print("veri yok")
        return render(request,'anasayfa.html')
    else:
        return render(request,'anasayfa.html',{'data' : posts_data})

def gotopost(request,postid):
    posts_data = Posts.objects.filter(id =postid)

    return render(request,'postdetail.html',{'detail':posts_data})





    


        