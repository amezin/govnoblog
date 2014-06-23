from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from govnoblog.models import Post
from govnoblog.forms import NewPostForm

def userlist(request):
    return render(request, 'userlist.html', {'users': User.objects.all()})

def postlist(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'postlist.html', {'by_user': user, 'posts': posts})

@login_required
def newpost(request, **kwargs):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        try:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return myposts(request)
        except ValueError:
            pass
    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {'form': form})

@login_required
def myposts(request):
    return HttpResponseRedirect(reverse('postlist', kwargs={'username': request.user.get_username()}))

