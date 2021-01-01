
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from mainapp.forms import SignUpFormForm ,EventAlumnimeetform
from mainapp.models import SignUpForm,EventAlumniMeet
from django.core.mail import send_mail
from django.conf import settings
import datetime
from django.db import connection
import sqlite3
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

def sign_up(request):
    signupform= SignUpFormForm()
    return render(request,"signup.html",{'form':signupform}) 

def successfullSignup(request):
	form = request.POST.copy()
	del form['csrfmiddlewaretoken']
	del form['action']

	form = form.dict()

	for key in form.keys():
		form[key] = form[key]

	SignUpForm.objects.create(**form)


	UserData = form
	Name=str(UserData.pop('Name'))
	Batch=str(UserData.pop('Batch'))
	Branch=str(UserData.pop('Branch'))
	Mobile=str(UserData.pop('Mobile'))
	Address=str(UserData.pop('Address'))
	Email=str(UserData.pop('Email'))
	Admin="http://127.0.0.1:8000/admin/"
	send_mail(
    'New ALUMNI REQUEST',
    Name+"\n"+ Batch + " \n" + Branch +"\n "+ Mobile + "\n "+ Address + " \n" + Email + " \n Please verfiy this Request and Provide them login Id  and Password.\n"+ Admin,
    'nandan980633@gmail.com',
    ['nandan98063@gmail.com'],
    fail_silently=False,
    )
	context={'NAME':Name,'Mail':Email}
	return render(request,"signupsucees.html",context)

# function for returning faq 
def faq(request):
	return render(request,"faq.html")

def BCETIANSEVENTS(request):
	return render(request,"BCETIANSEVENTS.html")

@login_required
def EventAlumniMeetR(request):
	form=EventAlumnimeetform(request.POST or None)
	
	return render(request,"EVENTREGISTER.html",{'form':form})

@login_required
def ThankYouPage(request):
	form = request.POST.copy()
	del form['csrfmiddlewaretoken']
	del form['action']

	form = form.dict()

	for key in form.keys():
		form[key] = form[key]

	EventAlumniMeet.objects.create(**form)
	return render(request,'eventsucessfull.html')

@login_required
def Profile_Page(request):
	
	return render(request,'Profile_Page.html')

	


