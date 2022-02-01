from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm
from django.urls import reverse


class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# Create your views here.
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article,id=id_)

class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = 'articles/article_update.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article,id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article,id=id_)   

    def get_success_url(self):
        return reversed('articles:article-list') 
