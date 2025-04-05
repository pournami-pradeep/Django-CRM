from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Record


class UserSignUpForm(UserCreationForm):
    helptext_pass1 = '''
    <ul class="form-text text-muted small">
    <li>Your password can\'t be too similar to your other personal information.</li>
    <li>Your password must contain at least 8 characters.</li>
    <li>Your password can\'t be a commonly used password.</li>
    <li>Your password can\'t be entirely numeric.</li></ul>
    '''

    helptext_pass2 = '''
    <span class="form-text text-muted small">Enter password as before.</span>
    '''
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Email"}))
    first_name = forms.CharField(label="First Name", max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"First Name"}))
    last_name = forms.CharField(label="Last Name", max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Last Name"}))
    username = forms.CharField(label="Username", max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}) ,help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>')
    password1 = forms.CharField(label="Password", max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),help_text=helptext_pass1)
    password2 = forms.CharField(label="Confirm Password", max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),help_text=helptext_pass2)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ["first_name","last_name","email","phone","address","city","state","zipcode"]
