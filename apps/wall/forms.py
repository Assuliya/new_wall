from django import forms
from .models import User
from django.core.exceptions import ValidationError
import bcrypt, re
PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    def clean_password(self):
        super(forms.ModelForm, self).clean()
        data = self.cleaned_data
        if not PASS_REGEX.match(data['password']):
            raise ValidationError('Password should contain at least one apper case letter and one number')
        else:
            data['password'] = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            return data['password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
