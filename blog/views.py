from django.shortcuts import render, get_object_or_404
from .models import blogPost
# Create your views here.

def blogs(request, slug):
    obj = get_object_or_404(blogPost, slug=slug)
    context = {'object' : obj}
    return render(request, 'blog.html',context)

def blogsList(request):
    blogList = blogPost.objects.all()
    context = {'objectList': blogList}
    return render(request, 'blogList.html', context)
