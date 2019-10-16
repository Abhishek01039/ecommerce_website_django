from django.shortcuts import render
from django.http import HttpResponse
from .models import blogspot
# Create your views here.


def index(request):
    Blogspot=blogspot.objects.all()
    params={'blog':Blogspot}
    return render(request, 'blog/index.html',params)



def blog(request, id):
    blogspot1=blogspot.objects.filter(post_id=id)[0]
    print(blogspot1)
    return render(request, 'blog/blogspot.html',{'post':blogspot1})


