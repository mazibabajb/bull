from email import message
from multiprocessing import context
from django.core.paginator import Paginator , EmptyPage
from django.shortcuts import render
from.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    sigs_cat = request.GET.get('p')
    if sigs_cat == None:
        sigs = Analyse.objects.get_queryset().order_by('id')
    else:
        sigs = Analyse.objects.filter(signal_category__name=sigs_cat)	

    signal_category = Sig_cat.objects.all()
    page_num = request.GET.get('page', 1)
    p = Paginator(sigs, 3)

    try:
        page = p.page(page_num)

    except EmptyPage:
        page = p.page(1)

    context = {
        "sig_cat" :signal_category,
        "sig": page,
        
    }
    return render(request,"index.html",context)

 
def analysis_detail(request, id):
    posts = Analyse.objects.get(id=id)
    blog_category = Sig_cat.objects.all()
    

    context = {
        'post':posts,
        "blog_cat" :blog_category,
	}
    return render(request, "single_analy.html",context)       



def about(request):
    return render(request,"about.html")

def pricing(request):
    return render(request,"pricing.html")    

def analysis(request):
    return render(request,)

def contact(request):
    if request.method == 'POST':
        contact = Contact_us()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Your message has been sent we will contact you as ppossible')
    return render(request,"contact.html")     

def team(request):
    return render(request,"team.html")  

def blog(request):
    recent = blog_post.objects.filter(is_trending=True)
    cat = request.GET.get('cat')
    if cat == None:
        posts = blog_post.objects.get_queryset().order_by('id')
    else:
        posts = blog_post.objects.filter(category_id__name=cat)	

    blog_category = category.objects.all()
    page_num = request.GET.get('page', 1)
    p = Paginator(posts, 3)

    try:
        page = p.page(page_num)

    except EmptyPage:
        page = p.page(1)

    context = {
        "blog_cat" :blog_category,
        "post": page,
        "recent_blog": recent
    }
    return render(request,"blog.html" ,context)


def post_detail(request, id):
    posts = blog_post.objects.get(id=id)
    blog_category = category.objects.all()
    recent = blog_post.objects.filter(is_trending=True)

    context = {
        'post':posts,
        "blog_cat" :blog_category,
        "recent_blog": recent,
	}
    return render(request, "blog-single.html",context)    


def blogsearchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = blog_post.objects.all().filter(title=search)
        return render(request,"seach.html",{'posts':posts})


def emailsubscription(request):
    if request.method == 'POST':
        email_sub = Email()
        email = request.POST.get('email')
        email_sub.email = email
        email_sub.save()
        messages.success(request, 'Thank you for subscribing for our newsletters')
    return render(request,"index.html")    
