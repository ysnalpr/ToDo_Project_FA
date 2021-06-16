from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .forms import ProfileForm, SignupForm
from .models import User
from .tokens import account_activation_token


class Profile(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'account/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')
    success_message = "تغییرات با موفقیت ذخیره شد."

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class SignUpUser(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی حساب کاربری'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال سازی ایمیل کاربری به ایمیل شما ارسال شد. <a href="/login">ورود</a>')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('حساب کاربری شما فعال شد. برای ورود <a href="/login">کلیک </a> کنید.')
    else:
        return HttpResponse('لینک فعال سازی نامعتبر است! <a href="/register">دوباره امتحان کنید</a>')

def error_404(request, exception):
        return render(request,'account/error_404.html', {})