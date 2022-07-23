from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from django.contrib.auth.views import (
  LoginView,
  LogoutView,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def home(request):
  return redirect("auth:login")
  # return render(request, 'authentication/index.html')


class CustomLoginView(LoginView):
  '''Custom Login View'''
  template_name = 'authentication/auth.html'
  fields = '__all__'
  redirect_authenticated_user = True
  
  def get_success_url(self):
    return reverse('library:home')

class CustomLogoutView(LogoutView):
  '''Custom Login View'''
  template_name = 'authentication/logged_out.html'
  
  def get_success_url(self):
    return reverse('library:home')


class CustomRegisterView(FormView):
  template_name = 'authentication/auth.html'
  form_class = UserCreationForm
  
  def get_success_url(self):
    return reverse('library:home')
  
  def form_valid(self, form):
    print(form.cleaned_data)
    user = form.save()
    print("Register form user", user)
    if user is not None:
      login(self.request, user)
    return super().form_valid(form)
  
  # Redirects the user if is_authenticated
  # def get(self, *args, **kwargs):
  #   if self.request.user.is_authenticated:
  #     return redirect('library:home')
  #   return super().get(*args, **kwargs)