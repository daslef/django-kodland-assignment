from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите название статьи'}), label='')
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')