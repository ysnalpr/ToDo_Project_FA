from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='نام')
    email = forms.EmailField(required=True, label='ایمیل', help_text='پاسخ شما به این ایمیل ارسال خواهد شد.')
    subject = forms.CharField(max_length=100, required=True, label='موضوع')
    message = forms.CharField(widget=forms.Textarea, required=True, label='پیام شما')
