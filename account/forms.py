from django import forms
from django.contrib.auth.forms import UserCreationForm

from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

from .models import User

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['date_of_birth'] = JalaliDateField(label=('تاریخ تولد'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget, required=False # optional, to use default datepicker
        )
        
        self.fields['username'].help_text = None
        if not user.is_superuser:
            self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'image']


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=200)

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']