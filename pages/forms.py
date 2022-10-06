from django import forms

class ContactForm(forms.Form):

    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your Email Address')
    subject = forms.CharField(max_length=100, label="subject")
    message = forms.CharField(widget=forms.Textarea)

