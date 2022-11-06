from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from valavio.accounts.forms import CreateProfileForm
from valavio.common.view_mixins import RedirectToDashboard

class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    # success_url = reverse_lazy('dashboard')
    #
    # def get_success_url(self):# дали има url, ако не дай дефолтния
    #     if self.success_url:
    #         return self.success_url
    #     return super().get_success_url()
    pass