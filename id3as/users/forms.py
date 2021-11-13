from django import forms
from django.contrib.auth import get_user_model, forms as auth_forms

User = get_user_model()


class UserCreationForm(auth_forms.UserCreationForm):
    """Form used to create new users."""

    class Meta(auth_forms.UserCreationForm.Meta):
        model = User


class UserChangeForm(auth_forms.UserChangeForm):
    """Form used to update user infos."""

    class Meta(auth_forms.UserChangeForm.Meta):
        model = User
