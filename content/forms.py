from django import forms

from content.models import Post


class new_entry_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class write_response_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']