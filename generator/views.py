from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	context={
	'password':'new password'
	}
	return render(request,'generator/index.html',context)

def password(request):

	characters=list('abcdefghijklmnopqrstuvwxyz')

	if request.POST.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.POST.get('special'):
		characters.extend(list('!@#$&*?'))
	if request.POST.get('numbers'):
		characters.extend(list('0123456789'))


	length=int(request.POST.get('length'))
	thepassword=''
	for x in range(length):
		thepassword += random.choice(characters)

	context={
	'password':thepassword
	}
	return render(request,'generator/password.html',context)