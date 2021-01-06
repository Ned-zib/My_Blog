from django import forms


class EmailPostForm(forms.Form):
    # this use a regular input HTML element <input type="text">
    name = forms.CharField(max_length=25)

    email = forms.EmailField()
    to = forms.EmailField()

    # we can change the default widget with the widged atribute
    comments = forms.CharField(required=False, widget=forms.Textarea)
