import random
import secrets
import string

from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm, UserResetPasswordForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        verify_code = ''.join([str(random.randint(0, 9)) for i in range(6)])
        user.verification_code = verify_code
        user.save()
        link = f"http://{self.request.get_host()}/users/verify/{verify_code}/"
        message = f"Для подтверждения регистрации перейдите по ссылке: {link}"
        send_mail(
            "Регистрация",
            message,
            EMAIL_HOST_USER,
            [user.email],
            False
        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('main:catalog')

    def get_object(self, queryset=None):
        return self.request.user


def verify_user(request, verify_code):
    for user in User.objects.all():
        if user.verification_code == verify_code:
            user.is_active = True
            user.save()
    return redirect(reverse_lazy('users:login'))


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('main:catalog')


class UserResetPasswordView(PasswordResetView):
    template_name = 'users/reset_password.html'
    form_class = UserResetPasswordForm
    success_url = reverse_lazy('users:login')
    email_template_name = 'users/password_reset_email.html'

    def form_valid(self, form):
        email = self.request.POST['email']
        try:
            user = User.objects.get(email=email)
            alphabet = string.ascii_letters + string.digits
            password = "".join(secrets.choice(alphabet) for i in range(12))
            user.set_password(password)
            user.save()
            message = f"Ваш новый пароль: {password}"
            send_mail(
                "Смена пароля",
                message,
                EMAIL_HOST_USER,
                [user.email],
                False
            )
        except User.DoesNotExist:
            return render(self.request, 'users/login.html',
                          {'error_message': 'Пользователь с таким email не найден'})
        return super().form_valid(form)
