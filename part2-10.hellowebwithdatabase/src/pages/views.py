from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	pk = request.GET.get('id')
	content = Message.objects.get(id=pk).content
		
	return HttpResponse(content)
