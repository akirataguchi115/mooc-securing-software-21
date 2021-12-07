from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account


@login_required
def transferView(request):
	
	if request.method == 'POST':
		with transaction.atomic():
			to = User.objects.get(username=request.POST.get('to'))
			sender = User.objects.get(username=request.user)
			acc1 = Account.objects.get(user=to)
			acc2 = Account.objects.get(user=sender)
			amount = int(request.POST.get('amount'))
		
			if (amount < 0):
				raise Exception()
			if (acc2.balance < amount):
				raise Exception()
 
			acc2.balance -= amount
			acc1.balance += amount
 
			acc2.save()
			acc1.save()
	
	return redirect('/')



@login_required
def homePageView(request):
	accounts = Account.objects.exclude(user_id=request.user.id)
	return render(request, 'pages/index.html', {'accounts': accounts})
