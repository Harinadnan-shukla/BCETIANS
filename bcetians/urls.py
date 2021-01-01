"""bcetians URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url
from mainapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^Homepage$',views.index,name='Homepage'),
    url(r'^sign_up$',views.sign_up,name='sign_up'),
   
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("successfull",views.successfullSignup,name="suceesfullsignup"),
    path("FAQ",views.faq,name="FAQ"),
    path("BCETIANSEVENTS",views.BCETIANSEVENTS,name="BCETIANSEVENTS"),
    url(r'^CONVOCATION/REGISTRATION$',views.EventAlumniMeet,name="CONVOCATION/REGISTRATION"),
    url(r'^$',views.Profile_Page, name='Profile_Page'),
    url(r'^EventAlumniMeetR$',views.EventAlumniMeetR,name="EventAlumniMeetR"),
    path("ThankYouPage",views.ThankYouPage,name="ThankYouPage"),

    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
   
    
]
