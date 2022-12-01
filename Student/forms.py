from .models import Student
from django import forms
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= ('name','Branch','Year')
        #fields='__all__'

class LoginForm(forms.Form):
    username= forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegform(forms.ModelForm):
    password = forms.CharField(label = 'Password',widget=forms.PasswordInput)
    conf_password = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=('username','email','first_name','last_name')
    def clean_conf_pass(self):
        cd =self.cleaned_data
        if cd['password']!=cd['conf_password']:
            raise forms.ValidationError('Password Should be same')
        return cd['conf_password']