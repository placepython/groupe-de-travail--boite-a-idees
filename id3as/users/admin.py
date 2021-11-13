from django.contrib import admin
from django.contrib.auth import get_user_model, admin as auth_admin

from .forms import UserCreationForm, UserChangeForm

User = get_user_model()


class UserAdmin(auth_admin.UserAdmin):
    """User administration using Custom User and Custom user forms."""

    model = User
    add_form = UserCreationForm
    form = UserChangeForm
