from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput(
        attrs={'class': 'parent'}), required=False)

    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        self.article = kwargs.pop('article')   # the blog entry instance
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        comment = super(CommentForm, self).save(commit=False)
        comment.article = self.article
        comment.save()
        return comment
