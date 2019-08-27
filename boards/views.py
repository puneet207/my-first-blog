from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board
from django.utils import timezone
from .forms import PostForm

def home(request):
    return HttpResponse('Hello, world!!')

def post_list(request):
    posts = Board.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'boards/post_list.html', {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'boards/post_edit.html', {'form': form})