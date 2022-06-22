from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Report, Quiz


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'core/home.html', context)

def quiz(request):
    if request.method == 'POST':
        sleep = request.POST['sleep']
        cook = request.POST['cook']
        loner = request.POST['loner']

        quiz = Quiz.objects.create(
            sleep=sleep,
            cook=cook,
            loner=loner
        )
        quiz.save()

        context = {
            'quiz' : quiz.pk
        }

        return render(request, 'core/post_form.html', context)
    
    return render(request, 'core/quiz.html')

class PostListView(ListView):
    model = Post
    template_name = 'core/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'start_year', 'start_month', 'end_year', 'end_month', 'budget', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'start_year', 'start_month', 'end_year', 'end_month', 'budget', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    template_name = 'core/report.html'
    fields = ['username_to_report', 'details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)