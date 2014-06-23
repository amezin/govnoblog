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
        if form.is_valid():
            Post.objects.create(user=request.user, content=form.cleaned_data['content'])
            return HttpResponseRedirect(reverse('postlist', kwargs={'username': request.user.get_username()}))
    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {'form': form})

