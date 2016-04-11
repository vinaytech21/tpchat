from django.shortcuts import render
from .models import Service
from products.models import Product
from .forms import ServiceForm, OfferForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import *
from profiles.models import BaseProfile
from profiles.views import *
from django.views.generic.list import ListView

class servicelistListView(ListView):
    model = Product
    model = Service

    template_name = 'services/service_home.html'  # optional (the default is app_name/modelNameInLowerCase_list.html; which will look into your templates folder for that path and file)
    post = Service.objects.all()
    paginate_by = 2


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

            return HttpResponseRedirect(reverse('services:offer_detail_service', args=(newdoc.pk,)))
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
            return HttpResponseRedirect(reverse('services:offer_detail_service', args=(post.pk,)))

    else:
        form = OfferForm(instance=post)
    return render(request,
	'services/service.html', { 'form': form})

@login_required
def service_history(request):
    model = Service
    posts = Service.objects.filter(user_id = request.user.id)
    return render(request, 'services/service_list.html', {'posts': posts })

def active(request):
    model = Service
    profile = get_object_or_404(models.Profile,user_id=request.user.id)
    user = profile.user
    post =  Service.objects.filter(zip_Code = profile.zipcode)
    return render(request, 'services/service_active.html', {'post': post})

    
