from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(created_date__lte=timezone.now())
    qs = qs.order_by('-created_date')

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(pk=id)\
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, pk=id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })
