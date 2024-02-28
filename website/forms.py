from django import forms
from website.models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    subject = forms.CharField(required=False)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)
