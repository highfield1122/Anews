from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ContactForm(forms.Form):
    """お問い合わせフォーム"""

    # フィールド
    name = forms.CharField()
    email = forms.EmailField()
    title = forms.CharField()
    message = forms.CharField()