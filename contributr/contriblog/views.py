from django.views import generic

from . import models
from .forms import PostForm


# Generic view that lists all blog posts that has publish set to true.
class BlogIndex(generic.ListView):
    queryset = models.Post.objects.published()
    template_name = "contriblog/index.html"


# Generic view that displays each post.
class BlogDetail(generic.DetailView):
    model = models.Post
    template_name = "contriblog/detail.html"

# Generic view that lists every post with selected tag.
class TagDetail(generic.DetailView):
    model = models.Tag
    template_name = "contriblog/tag.html"
    slug_url_kwarg = "tag"

class postNew(generic.edit.FormView):
    template_name = "contriblog/post_edit.html"
    form_class = PostForm
    success_url = '../'

    def form_valid(self, form):
        form.save()
        return super(postNew, self).form_valid(form)

class editForm(generic.edit.UpdateView):
    template_name = 'contriblog/post_edit.html'
    form_class = PostForm
    succes_url = '../'

    def form_valid(self, form):
        form.save()
        return super(editForm, self).form_valid(form)
