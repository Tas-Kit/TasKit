"""TasKit URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from views import (
    HomeView,
    LoginView,
    SignupView,
    ResetPasswordView,
    ResetPasswordDoneView,
    ResetPasswordConfirmView,
    ResetPasswordCompleteView
)

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^reset_password/$', ResetPasswordView.as_view(), name='reset_password'),
    url(r'^reset_password/done/$', ResetPasswordDoneView.as_view(), {'template_name': 'basic/reset_password_done.html'}, name='reset_password_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset_password/complete/$', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
]
