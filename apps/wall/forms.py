from django import forms
from .models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import bcrypt, re
PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_email(self):
        data = self.cleaned_data
        match = User.objects.filter(email=self.cleaned_data['email'])
        if match:
            raise ValidationError("This email address already exists")
        return data['email']

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

    def clean_email(self):
        data = self.cleaned_data
        try:
            user = User.objects.get(email=data['email'])
            print ('email is good')
            return data['email']
        except ObjectDoesNotExist:
            raise ValidationError("This Email does not exists")
    def clean_password(self):
        data = self.cleaned_data
        if self.is_valid():
            user = User.objects.get(email=data['email'])
            saved = user.password.encode()
            testing = data['password'].encode()
            if bcrypt.hashpw(testing, saved) == saved:
                print ('all good')
                return data['password']
            print ('email matched')
            raise ValidationError("The Password is wrong")
        return data['password']
