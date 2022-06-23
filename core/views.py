from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Report


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'core/home.html', context)

def quiz(request):
    if request.method == 'POST':
        sleep = request.POST.get('sleep', None)
        cook = request.POST.get('cook', None)
        loner = request.POST.get('loner', None)

        print(sleep)
        print(cook)
        print(loner)

        quiz = Quiz.objects.create(
            sleep=sleep,
            cook=cook,
            loner=loner,
        )

        quiz.save()

        print(request.path)

        return redirect("home")
    
    return render(request, 'core/quiz.html')


# class QuizView(CreateView):
#     model = Quiz
#     fields = ['sleep', 'cook', 'loner']

class PostListView(ListView):
    model = Post
    template_name = 'core/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'start_year', 'start_month', 'end_year', 'end_month', 'budget', 'location', "what_time_do_you_go_to_sleep", "how_often_do_you_cook_per_week", "how_often_do_you_meet_friends_per_week"]

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