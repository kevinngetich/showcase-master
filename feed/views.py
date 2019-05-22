from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from article.models import Article, Comments
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from article.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render




class FeedsView(generic.ListView):
    template_name = 'feed/index.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return Article.objects.all()

class DetailView(generic.DetailView):
    context_object_name = 'article'
    template_name = 'article/article.html'
    form_class = CommentForm
    #queryset = Article.objects.all()
    model = Article

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        #context['form'] = self.form_class
        return context

    def post(self, request, pk):
        #form = CommentForm(request.POST)

        if request.method == 'POST':
            article_id = request.POST.get('article')
            user_id = request.POST.get('user', False)
            commenttxt = request.POST.get('comment', False)
            print("User ID is: " + str(user_id))
            print("Comment is: " + str(commenttxt))
            print("Article is: " + str(article_id))
            articleinst = Article.objects.get(pk=article_id)
            newcomment = Comments()
            newcomment.article = articleinst
            newcomment.user = user_id
            newcomment.comment = commenttxt
            newcomment.save()
        return super().get(request)


def logout(request):
    auth_logout(request)
    return redirect('/')

class ArticleCreate(CreateView):
    model = Article
    fields = ['article_title', 'article_text', 'article_image']

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['article_title', 'article_text', 'article_image']

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('feed:index')

    def get(self, request, *args, **kwargs):
        return self.Article(request, *args, **kwargs)
