from django.shortcuts import render
from django.contrib.auth.models import User

def homePageView(request):
	return render(request, 'pages/index.html')

def changeUsernameView(request):
	user = User.objects.get(username='admin')
	user.set_password('admin')
	user.save()
	return render(request, 'pages/index.html')