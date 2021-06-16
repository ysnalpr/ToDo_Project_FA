from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = f"موضوع: {form.cleaned_data['subject']}"
            message = f"اسم: {name}\nپیام: {form.cleaned_data['message']} \n {email}"
            try:
                messages.success(request, 'ایمیل شما با موفقیت ارسال شد. درکوتاه ترین زمان ممکن به شما پاسخ داده خواهد شد.')
                send_mail(subject=subject, message=message, from_email=email, recipient_list=['todomanager04@gmail.com'])
            except BadHeaderError:
                return HttpResponse("ایمیل شما ارسال نشد!")
            return redirect('contact:contact')
    return render(request, 'contact/contact_form.html', {'form': form})
