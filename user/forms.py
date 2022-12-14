
from dataclasses import fields
from django import forms
from persian import convert_fa_numbers

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from place.models import Place
# from .models import Person
# from .permissions import reporter,registrar,administrator


class AccountForm(forms.Form):

    search=forms.CharField(max_length=100)


class CreateUserForm(forms.ModelForm):

    password=forms.CharField(max_length=30)

    class Meta:
        model=get_user_model()
        fields=[
            'first_name','last_name','password',
            'username','add','edit','delete','role','change_status'
        ]

    def save(self):
        user=super().save()
        user.username=convert_fa_numbers(self.cleaned_data.get('username')) 
        user.set_password(self.cleaned_data.get('password'))
        if self.cleaned_data.get('role') == 'administrator':
            user.add=True
            user.edit=True
            user.delete=True
            user.change_status=True
        # if self.cleaned_data.get('role') == 'reporter':
        #     reporter(user=user)
        # if self.cleaned_data.get('role') == 'registrar':
        #     registrar(user=user,data=self.cleaned_data)
        user.save()
        return user

class EditAccountForm(forms.ModelForm):

    class Meta:
        model=get_user_model()
        fields=[
            'first_name','last_name','username','add',
            'edit','delete','role','change_status'
        ]

    def save(self):
        user=super().save()
        user.username=convert_fa_numbers(self.cleaned_data.get('username')) 
        if self.cleaned_data.get('role') == 'administrator':
            user.add=True
            user.edit=True
            user.delete=True
            user.change_status=True
        # if self.cleaned_data.get('role') == 'reporter':
        #     reporter(user=user)
        # if self.cleaned_data.get('role') == 'registrar':
        #     registrar(user=user,data=self.cleaned_data)
        user.save()
        return user


class EditPasswordUserForm(UserCreationForm):

    old_password=forms.CharField(max_length=30)
    # new_password=forms.CharField(max_length=30)
    # conf_password=forms.CharField(max_length=30)

    class Meta:
        model=get_user_model()
        fields=['password1','password2','old_password']
