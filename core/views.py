from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Report
from .filters import PostFilter
from .models import Thread

def index(request):
    return render(request, 'core/index.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'core/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'core/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title',
              'content',
              'start_date',
              'end_date', 
              'search_location', 
              'studies_at', 
              'budget',
              'what_time_do_you_go_to_sleep', 
              'how_often_do_you_cook_per_week', 
              'how_often_do_you_meet_friends_per_week',
              'how_often_do_you_think_you_will_bring_other_people_into_the_flat',
              'when_do_you_usually_return_to_the_flat',
              'how_often_do_you_drink_alcohol',
              'when_do_you_shower',
              'how_often_do_you_shop_for_groceries',
              'how_often_do_you_do_chores']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title',
              'content',
              'start_date',
              'end_date', 
              'search_location', 
              'studies_at', 
              'budget',
              'what_time_do_you_go_to_sleep', 
              'how_often_do_you_cook_per_week', 
              'how_often_do_you_meet_friends_per_week',
              'how_often_do_you_think_you_will_bring_other_people_into_the_flat',
              'when_do_you_usually_return_to_the_flat',
              'how_often_do_you_drink_alcohol',
              'when_do_you_shower',
              'how_often_do_you_shop_for_groceries',
              'how_often_do_you_do_chores']

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

def search_result(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'core/search_result.html', {'searched':searched, 'posts':posts})
    else:
        return render(request, 'core/search_result.html', {})

def filter(request):
    if request.method == "POST":
        available = Post.objects.all()

        try:
            budget = int(request.POST["budget"])
            available = Post.objects.filter(budget__lte=budget+100).filter(budget__gte=budget-100)
        except:
            pass

        sleep = int(request.POST["what_time_do_you_go_to_sleep"])
        if sleep != 0:
            print("Available:\n" + str(available))
            print("I'm filtering sleep")
            available = available.filter(what_time_do_you_go_to_sleep=sleep)

        cook = int(request.POST["how_often_do_you_cook_per_week"])
        if cook != 0:
            available = available.filter(how_often_do_you_cook_per_week=cook)

        loner = int(request.POST["how_often_do_you_meet_friends_per_week"])
        if loner != 0:
            available = available.filter(how_often_do_you_meet_friends_per_week=loner)

        context = {
            'posts': available
        }

        return render(request, 'core/home.html', context)
    return render(request, "core/filter_form.html")

class FaqView(LoginRequiredMixin, CreateView):
    model = Report
    template_name = 'core/faq.html'
    fields = ['username_to_report', 'details']

@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'core/messages.html', context)