

from django import forms

class SearchForm(forms.Form):
    selected_class = forms.ChoiceField(choices=[
        ('owner', 'Owner'),
        ('car', 'Car'),
        ('gallery', 'Gallery'),
        ('all', 'All')
    ])
    selected_value = forms.CharField(required=False)  # İsteğe bağlı alan
