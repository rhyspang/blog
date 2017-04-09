from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='username',
        error_messages={'required': "Username field is required"},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
            },
        ),
    )

    password = forms.CharField(
        required=True,
        label='Password',
        error_messages={'required': 'Password field is required'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password field is required',
            },
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('username or password error')
        else:
            self.cleaned_data = super(LoginForm, self).clean()

