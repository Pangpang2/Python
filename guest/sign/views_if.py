from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.db.utils import IntegrityError

def add_event(request):
	eid = request.POST.get('eid','')
	name = request.POST.get('name', '')
	limit = request.POST.get('limit','')
	status = request.POST.get('status','')
	address = request.POST.get('address', '')
	start_time = request.POST.get('start_time','')

	if eid =='' or name =='' or limit =='' or address =='' or start_time=='':
		return JsonResponse({'status':10021,'message':'parameter error'})

	result = Event.objects.filter(id = eid)

	if result:
		return JsonResponse({'status':10022,'message':'event id already exists'})

	result = Event.objects.filter(name = name)

	if result:
		return JsonResponse({'status':10023,'message':'event name already exists'})

	if status == '':
		status = 1

	try:
		Event.objects.create(id=eid,name=name,limit=limit,address=address, status=int(status),start_time=start_tim)
	except ValidationError as e:
		error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
		return JsonResponse({'status':10024,'message':error})

	return JsonResponse({'status':200,'message':'add event success'})

def get_event_list(request):
	eid = request.GET.get('eid','')
	name = request.GET.get('name','')

	if eid == '' and name =='':
		return JsonResponse({'status':10021, 'message':'parameter error'})

	if eid !='':
		event = {}
		try:
			result = Event.objects.get(id = eid)
		except ObjectDoesNotExist:
			return JsonResponse({'status':10022,'message':'query result is empty'})
		else: 
			event['name'] = result.name
			event['limit'] = result.limit
			event['status'] = result.status
			event['address'] = result.address
			event['start_time'] = result.start_time
			return JsonResponse({'status':200,'message':'success','data': event})

	if name !='':
		data=[]
		results = Event.objects.filter(name__contains = name)
		if results:
			for r in results:
				event = {}
				event['name'] = r.name
				event['limit'] = r.limit
				event['status'] = r.status
				event['address'] = r.address
				event['start_time'] = r.start_time
				data.append(event)
			return JsonResponse({'status':200,'message':'success','data': data})
		else:
			return JsonResponse({'status':10022,'message':'query result is empty'})

def add_guest(request): 
	eid = request.POST.get('eid','') # 关联发布会id realname = request.POST.get('realname','') # 姓名 phone = request.POST.get('phone','') # 手机号 email = request.POST.get('email','') # 邮箱
	if eid =='' or realname == '' or phone == '': 
		return JsonResponse({'status':10021,'message':'parameter error'})
	result = Event.objects.filter(id=eid) 
	if not result: 
		return JsonResponse({'status':10022,'message':'event id null'})

	result = Event.objects.get(id=eid).status 
	if not result: 
		return JsonResponse({'status':10023, 'message':'event status is not available'})
	
	event_limit = Event.objects.get(id=eid).limit # 发布会限制人数 guest_limit = Guest.objects.filter(event_id=eid) # 发布会已添加的嘉宾数
	if len(guest_limit) >= event_limit: 
		return JsonResponse({'status':10024,'message':'event number is full'})

	event_time =Event.objects.get(id = eid).start_time
	etime = str(event_time).split(".")[0]
	timeArray = time.strptime(etime,"%Y-%m-%d %H:%M:%S")
	e_time = int(time.mktime(timeArray))

	now_time = str(time.time())
	ntime = now_time.split(".")[0]
	n_time = int(ntime)

	if n_time >= e_time:
		return JsonResponse({'status':10025,'message':'event has started'})
	
	try: 
		Guest.objects.create(realname=realname,phone=int(phone),email=email, sign=0,event_id=int(eid)) 
	except IntegrityError: 
		return JsonResponse({'status':10026, 'message':'the event guest phone number repeat'})

	return JsonResponse({'status':200,'message':'add guest success'}) 

