from django.forms import ModelForm, Textarea
from govnoblog.models import Post

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'content': ''
        }
        widgets = {
            'content': Textarea(attrs={'cols': 80})
        }

