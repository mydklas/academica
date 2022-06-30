from django.shortcuts import render, get_object_or_404, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Post, Booking, Text
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import BookCreateForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.contrib import messages
# Create your views here.
# from django.http import HttpResponse

#@login_required
#@csrf_exempt
#def booking(request):
    #get_token(request)
    #return render(request,'klas/booking.html')



@login_required
# get_token(request)
@csrf_exempt
def booking(request):
    model = Booking
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            fn = form.cleaned_data['fname']
            ln = form.cleaned_data['lname']
            kl = form.cleaned_data['klas']
            ts = form.cleaned_data['time_schedule']
            ds = form.cleaned_data['date_started']
            book = Booking(fname=fn,lname=ln,klas=kl,time_schedule=ts,date_started=ds)
            book.save()
            # username = form.cleaned_data.get('username')

            messages.success(request, f'{fn} {ln} , Your booking has been created! ')
            context = {
                # 'form' : form
                'form' : form
            }
            return render(request,'klas/book_detail.html',context)
    else:
        form = BookCreateForm()

    return render(request, 'klas/booking.html', {'form':form })


def schedule(request):
    return render(request,'klas/schedule.html')


def admisi(request):
    return render(request,'klas/klaskoding.html')

def article(request):
    context = {
        'posts': Post.objects.all(),

    }
    return render(request, 'klas/article.html', context)

def home(request):

    context = {
        'posts': Post.objects.all,
    }
    return render(request, 'klas/home.html', context)

# def hometext(request):
#     context = {
#         'posts': Post.objects.all(),
#         'texts': Text.object.all()
#
#     }
#     return render(request, 'klas/home.html', context)

class TextListView(ListView):
    model = Text
    template_name = 'klas/home.html'
    context_object_name = 'texts'
    ordering = ['-date_teks']


class PostListView(ListView):
    model = Post
    template_name = 'klas/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class ArticleListView(ListView):
    model = Post
    template_name = 'klas/article.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'klas/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content','image_post','caption']

    def save(self, *args, **kwargs):
        super(PostCreateView, self).save(*args, **kwargs)

        img = Image.open(self.image_post.path)

        if img.height > 300 or img.width > 600:
            output_size = (300, 600)
            img.thumbnail(output_size)
            img.save(self.image_post.path)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content','image_post','caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def save(self, *args, **kwargs):
        super(PostUpdateView, self).save(*args, **kwargs)

        img = Image.open(self.image_post.path)

        if img.height > 300 or img.width > 600:
            output_size = (300, 600)
            img.thumbnail(output_size)
            img.save(self.image_post.path)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class TextCreateView(LoginRequiredMixin,CreateView):
    model = Text
    fields = '__all__'
    template_name = 'klas/teks_form.html'
    context_object_name = 'texts'

    def save(self, *args, **kwargs):
        super(TextCreateView, self).save(*args, **kwargs)

        img = Image.open(self.image_teks.path)

        if img.height > 300 or img.width > 600:
            output_size = (300, 600)
            img.thumbnail(output_size)
            img.save(self.image_teks.path)

    def form_valid(self, form):
        form.instance.author_teks = self.request.user
        return super().form_valid(form)