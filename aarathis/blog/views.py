from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm
# Create your views here.
#static demo data which was used before the blog advanced like beginning
#posts = [
#       {'id':1,'title': 'Post 1', 'content': 'Content of Post 1'},
#       {'id':2,'title': 'Post 2', 'content': 'Content of Post 2'},
#       {'id':3,'title': 'Post 3', 'content': 'Content of Post 3'},
#       {'id':4,'title': 'Post 4', 'content': 'Content of Post 4'},
        
#       ]
def index(request):
    blog_title = "Latest posts"
    #getting data from post model
    all_posts = Post.objects.all()

    #paginate
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'blog_title': blog_title, 'page_obj': page_obj})

def detail(request, post_id):
    #static data before using by getting id from each post by url
    #post=next((item for item in posts if item ['id'] == int(post_id)), None)
    #getting data from model by post id 
    post = get_object_or_404(Post,pk=post_id)
    related_posts = Post.objects.filter(category = post.category).exclude(pk=post_id)
    #logger = logging.getLogger("TESTING")
    #logger.debug(f'post variable is {post}')
    return render(request, 'detail.html', {'post':post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"POST DATA is {(form.cleaned_data['name'])} {(form.cleaned_data['email'])} {(form.cleaned_data['message'])}")
            #send email or save in database
            success_message = 'Your email has been sent!'
            return render(request, 'contact.html', {'form':form, 'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request, 'contact.html', {'form':form, 'name':name, 'email':email, 'message':message})
            
    return render(request, 'contact.html')


def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request, 'about.html',{'about_content':about_content})