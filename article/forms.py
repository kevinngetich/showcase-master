from django import forms

class CommentForm(forms.Form):
    article = forms.CharField(widget = forms.HiddenInput())
    username = forms.CharField(widget = forms.HiddenInput())
    comment = forms.CharField(widget=forms.Textarea)