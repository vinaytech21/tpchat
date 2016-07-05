from django.views import generic
from django.shortcuts import render
import django
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from products.models import Product
from services.models import Service
from events.models import Event
from profiles.models import BaseProfile
from profiles.views import *
from authtools.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

class HomePage(generic.TemplateView):
    template_name = "home.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

def faq(request):
	return render(request, "faq.html", {})

def conect(request):
	return render(request, "conect.html", {})

def term(request):
	return render(request, "term.html", {})

def tour(request):
	return render(request, "tour.html", {})


def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(title__icontains=q)
		events = Event.objects.filter(eventtype__icontains=q)
		services = Service.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products, 'services': services, 'events': events}
		template = 'results.html'	
	else:
		template = 'home.html'	
		context = {}
	return render(request, template, context)


@login_required
def zipcode(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(zip_Code__icontains=q)
		events = Event.objects.filter(zip_Code__icontains=q)
		services = Service.objects.filter(zip_Code__icontains=q)
		context = {'query': q, 'products': products, 'services': services, 'events': events}
		template = 'zipresult.html'	
	else:
		template = 'zipcode.html'	
		context = {}
	return render(request, template, context)


def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_name = form.cleaned_data.get("name")		
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")		
		# print email, message, full_name
		subject = 'Someone has touch UR App'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'vinaykumar.vk2007@gmail.com']
		contact_message = "Name: %s Message:%s  via %s"%( 
				form_name, 
				form_message,
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				fail_silently=True)

		return HttpResponseRedirect('/')

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "contact.html", context)

@login_required
def Zipuser(request, template_name='zipuser.html'):
    profile = get_object_or_404(models.Profile,user_id=request.user.id)
    user = profile.user
    data =  User.objects.filter(zipfield = user.zipfield)
    paginator = Paginator(data, 6)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    return render_to_response('zipuser.html', {
        'data': data, 
    }, context_instance=RequestContext(request))

@login_required
def zipuserdetail(request, pk):
    model = User
    data =  User.objects.filter(pk=pk)
    return render(request, 'zipuserdetail.html', {'data': data })




