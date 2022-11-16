
from django.forms import ModelForm


from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User

from . models import Thought, Profile



from django import forms 

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput


# - Create a new user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']



# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Post a thought

class ThoughtPostForm(forms.ModelForm):

    class Meta:

        model = Thought
        fields = ['title', 'content',]
        exlude = ['user']


# - Update a thought

class ThoughtUpdateForm(forms.ModelForm):

    class Meta:

        model = Thought
        fields = ['title', 'content',]
        exlude = ['user']


# - Update your username and email

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User

        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]


# - Update your profile picture

class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:

        model = Profile
        fields = ['profile_pic',]