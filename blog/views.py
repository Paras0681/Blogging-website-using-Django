from django.shortcuts import render
from django.urls.base import reverse_lazy
from  django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post
from .forms import PostForm, EditForm

# def home(request):
# 	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'addpost.html'
	# fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'updatepost.html'
# fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'deletepost.html'
	success_url = reverse_lazy('home')