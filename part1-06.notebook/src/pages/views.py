from django.shortcuts import render

# Create your views here.

def addPageView(request):
	items = request.session.get('items', [])
	item = request.POST.get('content', '').strip()
	if len(item) > 0:
		items.append(item)
	if len(items) > 10:
		del items[0]
	request.session['items'] = items
	return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
	items = []
	request.session['items'] = items
	return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
