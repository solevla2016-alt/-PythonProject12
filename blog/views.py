from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Blog
from blog.forms import BlogForm
from django.core.mail import send_mail
from django.conf import settings


class BlogListView(ListView):

    model = Blog

    template_name = "blog/blog_list.html"

    context_object_name = "object_list"

    def get_queryset(self):

        return Blog.objects.filter(
            is_published=True
        )

class BlogDetailView(DetailView):

    model = Blog
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):

        obj = super().get_object(queryset)

        obj.views_count += 1
        obj.save()

        # 👉 проверка 100 просмотров
        if obj.views_count == 100:

            send_mail(
                subject="Поздравляем!",
                message=f"Статья '{obj.title}' набрала 100 просмотров!",
                from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, "DEFAULT_FROM_EMAIL") else "test@localhost",
                recipient_list=["admin@example.com"],
                fail_silently=True,
            )

        return obj


class BlogCreateView(CreateView):

    model = Blog

    form_class = BlogForm

    success_url = reverse_lazy("blog:list")


class BlogUpdateView(UpdateView):
        model = Blog
        form_class = BlogForm
        template_name = "blog/blog_form.html"

        def get_success_url(self):
            return reverse("blog:detail", args=[self.object.pk])


class BlogDeleteView(DeleteView):

    model = Blog

    success_url = reverse_lazy("blog:list")