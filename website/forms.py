from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    subject = forms.CharField(required=False)
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)
