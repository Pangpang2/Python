from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	return render(request, "index.html")

def login_action(request):
	if request.method=='POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password = password)
		if user is not None:
			auth.login(request, user)
			#response.set_cookie('user', username, 3600)
			request.session['user'] = username
			response = HttpResponseRedirect('/event_manage/')
			request.session['user'] = username
			return response
		else:
			return render(request, 'index.html', {'error':'username or password error!'})
	else:
		return render(request, 'index.html', {'error': 'the request is using get method'})

@login_required
def event_manage(request):
	event_list = Event.objects.all()
	#username = request.COOKIES.get('user', '')
	username = request.session.get('user', '')
	return render(request, "event_manage.html", {'user':username, 'events': event_list})

@login_required
def search_name(request):
	username = request.session.get('user', '')
	search_name = request.GET.get("name", "")
	event_list = Event.objects.filter(name__contains=search_name)
	return render(request, "event_manage.html", {'user':username, 'events': event_list})

@login_required
def guest_manage(request):
	username = request.session.get('user','')
	guest_list = Guest.objects.all();
	paginator = Paginator(guest_list,2)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	return render(request, "guest_manage.html",{'user': username, 'guests': contacts})

@login_required
def sign_index(request, event_id):
	event = get_object_or_404(Event, id = event_id)
	total = Guest.objects.filter(event_id = event_id).count()
	signed = Guest.objects.filter(event_id = event_id, sign = '1').count()
	return render(request, 'sign_index.html', {'event':event,'total': total, 'signed':signed})

@login_required
def sign_index_action(request, event_id):
	event = get_object_or_404(Event, id = event_id)
	phone = request.POST.get('phone', '')

	total = Guest.objects.filter(event_id = event_id).count()
	signed = Guest.objects.filter(event_id = event_id, sign = '1').count()
	result = Guest.objects.filter(phone = phone, event_id = event_id)

	if not result:
		return render(request, 'sign_index.html', {'event':event, 'hint':'phone error.','total': total, 'signed':signed})

	result = Guest.objects.get(phone=phone, event_id = event_id)
	
	if result.sign:
		return render(request, 'sign_index.html', {'event':event, 'hint':'user has sign in.','total': total, 'signed':signed})

	else:
		Guest.objects.filter(phone=phone, event_id = event_id).update(sign='1')
		signed = signed + 1
		return render(request, 'sign_index.html', {'event':event,'hint':'sign in successful','guest':result, 'total': total, 'signed':signed})

@login_required
def logout(request):
	auth.logout(request)
	response = HttpResponseRedirect('/index/')
	return response