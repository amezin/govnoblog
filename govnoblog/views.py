from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from govnoblog.models import Post
from govnoblog.forms import NewPostForm

def userlist(request):
    return render(request, 'userlist.html', {'users': User.objects.all()})

def postlist(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'postlist.html', {'by_user': user, 'posts': posts})

@login_required
def newpost(request):
    return __editpost(request)

@login_required
def myposts(request):
    return HttpResponseRedirect(reverse('postlist', kwargs={'username': request.user.get_username()}))

def __getpost(request, postid):
    post = get_object_or_404(Post, pk=postid)
    if post.user != request.user:
        raise PermissionDenied()
    return post

def __editpost(request, instance=None):
    if request.method == 'POST':
        form = NewPostForm(request.POST, instance=instance)
        try:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return myposts(request)
        except ValueError:
            pass
    else:
        form = NewPostForm(instance=instance)
    return render(request, 'newpost.html', {'form': form})

@login_required
def edit(request, postid):
    return __editpost(request, __getpost(request, postid))

@login_required
def delete(request, postid):
    __getpost(request, postid).delete()
    return myposts(request)

