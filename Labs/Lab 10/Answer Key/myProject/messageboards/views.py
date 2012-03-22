from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from messageboards.models import Message
import hashlib, datetime

def register(request):
	if(request.method == 'POST'):
		try:
			u = User.objects.create_user(username=request.POST['user'],
				email='', password=request.POST['passwd'])
			u.is_staff = False
			u.save()
			return HttpResponseRedirect('/boards/')
		except: 
			return HttpResponse('Username already exists')
	else:
		return render_to_response('messageboards/register.html', {},
            context_instance=RequestContext(request))

def renderHome(request, user):
	try:
		m = Message.objects.values('page').distinct()
		t = loader.get_template('messageboards/list.html')
		c = RequestContext(request, {'mlists':m,'name':user})
		response = HttpResponse(t.render(c))
		response.set_cookie('id', hashlib.sha224(user).hexdigest())
		return response
	except:
		return render_to_response('messageboards/login.html', {},
			context_instance=RequestContext(request))

def login(request):
	if(request.method == 'POST'):
		u = {'username':request.POST['username'],
			'password':request.POST['password']}
		user = auth.authenticate(username=u['username'], password=u['password'])
		if user is not None:
			auth.login(request, user)
			response = renderHome(request, u['username'])
			return response
		else:
			return HttpResponse('Bad credentials')
	else:
		return default(request)

def logout(request):
	if request.user.is_authenticated():
		auth.logout(request)
		return HttpResponseRedirect('/boards/')
	else:
		return HttpResponseRedirect('/boards/')

def renderLogin(request):
	return render_to_response('messageboards/login.html', {},
		context_instance=RequestContext(request))

def create(request):
	if request.user.is_authenticated():
		return render_to_response('messageboards/create.html', {},
			context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/boards/')

def createThread(request):
	if (request.method == 'POST' and request.user.is_authenticated()):
		try:
			thread = Message(page=request.POST['threadname'], 
				user=request.user,
				message=request.POST['postdata'],
				time=datetime.datetime.now() )

			thread.save()

			response = renderHome(request, request.user.username)
			return response
		except:
			return HttpResponse('Post could not be created')
	else:
		return HttpResponseRedirect('/boards/')

def messages(request, inpage):
	if (request.user.is_authenticated() and request.user is not None):
		try: 
			if (request.method == 'POST'):
				print inpage, ":", request.user, ":" ,request.POST['postdata']
				reply = Message(page=inpage, 
					user=request.user, 
					message=request.POST['postdata'],
					time=datetime.datetime.now())
				reply.save()
			m = Message.objects.select_related().filter(page=inpage).order_by('time')
		except Message.DoesNotExist:
			m = None
		return render_to_response('messageboards/page.html',
			{'page':inpage, 'messages':m},
        			context_instance=RequestContext(request))
	else:
		return renderLogin(request)

def default(request):
	try:
		if (request.user.is_authenticated() and request.user is not None):
			response = renderHome(request, request.user.username)
			return response
		else:	
			return render_to_response('messageboards/login.html', {},
				context_instance=RequestContext(request))
	except: 
		return render_to_response('messageboards/login.html', {},
				context_instance=RequestContext(request))
