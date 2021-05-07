from django import forms

class NameForm(forms.Form):
    input = forms.CharField(label='input', max_length=100)

    def clean(self):
        super().clean()

