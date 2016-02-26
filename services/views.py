from django.shortcuts import render
from .models import Service
from .forms import ServiceForm, OfferForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import *

def servicelist(request):
    model = Service
    post = Service.objects.all()
    return render(request, 'services/service_home.html', {'post': post})

def service_detail_home(request, pk):
    model = Service
    #user_id=request.user.id
    post = get_object_or_404(Service, pk=pk)
    #document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, 'services/service_detail_home.html', {'post': post })

def offer(request):
     model = Service
     post = Service.objects.all()

     if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Service(user = request.user, title = request.POST['title'], docfile = request.FILES['docfile'], active = request.POST['active'], description = request.POST['description'], duraction = request.POST['duraction'], zip_Code = request.POST['zip_Code'], address = request.POST['address'], expire_date = request.POST['expire_date'])
            newdoc.save()
            return HttpResponseRedirect(reverse('services:offer_detail_service',args=(post.pk,)))
     else:
        form = ServiceForm() # A empty, unbound form


   # Load documents for the list page

     return render_to_response(
        'services/service.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


login_required
def offer_detail_service(request, pk):
    model = Service
    user_id=request.user.id
    #post = Product.objects.filter(user_id = request.user.id, pk=pk)
    post = get_object_or_404(Service, user_id=request.user.id, pk=pk)
    return render(request, 'services/offer_detail.html', {'post': post})



def edit_service(request, pk):
    model = Service
    post = get_object_or_404(Service, user_id=request.user.id, pk=pk)
    if request.method == "POST":
        form = OfferForm(request.POST, request.FILES, instance=post )
        if form.is_valid():
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('services:offer_detail_service',args=(post.pk,)))

    else:
        form = OfferForm(instance=post)
    return render(request,
	'services/service.html', { 'form': form})

@login_required
def service_history(request):
    model = Service
    posts = Service.objects.filter(user_id = request.user.id)
    return render(request, 'services/service_list.html', {'posts': posts })
    
