from django.shortcuts import render, redirect
from .models import PostModel, BlogCategory

# Create your views here.
def blog(request):
    context = {}
    posts = PostModel.objects.all()
    context['posts'] = posts
    return render(request, 'blog/blog.html', context)

def my_blog(request):
    context = {}
    user = request.user
    my_posts = PostModel.objects.filter(author=user)
    context['my_posts'] = my_posts
    return render(request, 'blog/my_blogs.html', context)


def create_blog(request):
    context = {}
    user = request.user
    obj = BlogCategory.objects.all()
    
    if request.method == 'POST':
        data = PostModel()
        data.title = request.POST.get('title')
        data.author = user
        data.body = request.POST.get('body')
        form_cat = request.POST['category']
        data.category = BlogCategory.objects.get(name=form_cat)
        
        if len(request.FILES) !=0:
            data.image = request.FILES['image']

        
        data.save()
        return redirect("my_blog")
        
    if request.method =='GET':
        
        context["category"] =obj
    
        return render(request, 'blog/create_blog.html', context)