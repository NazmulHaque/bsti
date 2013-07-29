from django import forms
from django.contrib import auth
from django.utils.translation import ugettext, ugettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    error_messages = {
        'invalid_login': _("Please enter a correct email and password."),
        'inactive': _("This account is inactive."),
        }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = auth.authenticate(username=username, password=password)
            if self.user_cache is None:
                self._errors["password"] = self.error_class([self.error_messages['invalid_login']])
                raise forms.ValidationError(self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                self._errors["email"] = self.error_class([self.error_messages['inactive']])

        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
