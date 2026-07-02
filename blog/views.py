from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView

from blog.forms import CommentaryForm
from blog.models import Post


def index(request):
    posts = Post.objects.order_by("-created_time")
    paginator = Paginator(posts, 5)  # 5 постів на сторінку

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/index.html", {
        "page_obj": page_obj,
        "post_list": page_obj.object_list
    })


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm(
            initial={"user": self.request.user}
        )
        return context
