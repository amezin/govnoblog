from django.forms import Form, CharField, Textarea

class NewPostForm(Form):
    content = CharField(label='', max_length=255, widget=Textarea())

