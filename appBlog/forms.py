from django import forms
from appBlog.models import Contact, Comment
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'

    def clean_name(self):
        return 'Anonymous'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message']
