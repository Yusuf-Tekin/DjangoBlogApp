from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    location = models.CharField(max_length = 25)
    profession = models.CharField(max_length = 20)#meslek
    myinterests = models.TextField()
    email = models.EmailField()
    aboutme = models.TextField()
    def __str__(self):
        return self.name


class Posts(models.Model):
    header = models.CharField(max_length = 120)
    content = models.TextField()
    postdata = models.DateField(auto_now_add = True)
    label = models.CharField(max_length = 200)
    image = models.TextField()
    author = models.CharField(max_length = 100)
    

    def __str__(self):
        return self.header



