from django.views import generic
from django.shortcuts import render
import django
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


def faq(request):
	return render(request, "faq.html", {})


def term(request):
	return render(request, "term.html", {})


def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_full_name = form.cleaned_data.get("full_name")		
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")		
		# print email, message, full_name
		subject = 'Someone has touch UR App'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'vinaykumar.vk2007@gmail.com']
		contact_message = "Name: %s Message:%s  via %s"%( 
				form_full_name, 
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




