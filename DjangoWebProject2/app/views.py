"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import poolForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .forms import CommentForm
from .models import Comment
from .forms import BlogForm


from .models import Blog


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Информация',
            'message':'Сведение о нас.',
            'year':datetime.now().year,
        }
    )

def useful_ar(request):
    """Renders the useful_ar page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/useful_ar.html',
        {
            'title':'Полезные статьи',
            'message':'Различные статьи, касаемые музыкальной индустрии.',
            'year':datetime.now().year
        }
    )

def pool_html(request):
	"""Renders the pool_html page."""
	assert isinstance(request, HttpRequest)
	data = None
	sex = {'1':'Мужской', '2':'Женский'}
	game = {'1':'RPG', '2':'Шутеры', '3':'Кампания'}

	if request.method == 'POST':
		form = poolForm(request.POST)
		if form.is_valid():
			data = dict()
			data['age'] = form.cleaned_data['age']
			data['sex'] = sex[form.cleaned_data['sex']]
			
			temp_str = ''
			for i in form.cleaned_data['game']:
				temp_str += game.get(i) + ' '
			data['game'] = temp_str

			form = None
	else:
		form = poolForm()
	return render(
		request,
		'app/pool_html.html',
		{
			 'title': 'Анкета',
			'form':form,
			'data':data
		}
	)

def registration(request):
    """Renders the registration page"""
    
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff =False

            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()

            regform.save()

            return redirect('home')

    else:
       regform = UserCreationForm()
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
        'regform': regform,

        'year': datetime.now().year,
        }
     )

def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() 

    return render(
        request,
        'app/blog.html',
       {

           'title':'Блог',
           'posts': posts, 
           'year':datetime.now().year,
            
            

   
        }
     )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id) 
    else:
        form = CommentForm() 
    
        return render(
        request,
        'app/blogpost.html',
      
       {
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year':datetime.now().year,
        
       }
        
    )

def newpost(request):
    """Renders the newpost page"""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user
            blog_f.save()

            return redirect('blog')
    else:
         blogform = BlogForm()

    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',

            'year':datetime.now().year,
        }

    )

def videopost(request):
    """Renders the videpost page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Информация',
            'message':'Загрузите',
            'year':datetime.now().year,
        }
    )