from django.urls import path, include
# from . import views
from . views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
urlpatterns = [
	# path('', views.home, name='home'),
	path('', HomeView.as_view(), name='home'),
	path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
	path('addpost/', AddPostView.as_view(), name='addpost'),
	path('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
	path('article/<int:pk>/remove', DeletePostView.as_view(), name='deletepost'),
]