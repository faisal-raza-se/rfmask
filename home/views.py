from django.shortcuts import render
from .models import AboutStaff, AboutFeatureCategory, AboutUs, Choose, Service, WorkProcess, Testimonial
from blog.models import PostModel

# Create your views here.

def index(request):
    features = AboutFeatureCategory.objects.all()
    about = AboutUs.objects.all()
    choose = Choose.objects.all()
    services = Service.objects.all()
    process = WorkProcess.objects.all()
    test = Testimonial.objects.all()
    staff = AboutStaff.objects.all()
    blog = PostModel.objects.all()
    
    context ={
        'features': features,
        'about': about,
        'choose': choose,
        'services': services,
        'process': process,
        'test': test,
        'staff': staff,
        'blog': blog,
    }
    return render(request, "home/index.html", context)

def about(request):
    
    features = AboutFeatureCategory.objects.all()
    about = AboutUs.objects.all()
    staff = AboutStaff.objects.all()
    context ={
        'features': features,
        'about': about,
        'staff': staff
    }
    return render(request, "home/about.html", context)

def contact(request):
    return render(request, "home/contact.html")
