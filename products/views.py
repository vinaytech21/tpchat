from django.shortcuts import render
from .models import Product
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.
from .forms import ProductForm, PostForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import *

# Create your views here.
class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print context
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")
        return context


#Basic search function
#using q import from django.db.models import Q
#
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
                )
            try:
                qs2 = self.model.objects.filter(
                Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs


################################################################################## for show detail of product mail and dashboard
#Product Detail view for showing detail of products............
class ProductDetailView(DetailView):
    model = Product
    def product_detail_view_func(request, id):
        product_instance =  get_object_or_404(Product, id=id)
        try:
            product_instance = Product.object.get(id=id)
        except Product.DoesNotExist:
            raise Http404
        except:
            raise Http404
        template = "products/product_detail.html"
        context = {
        "object": product_instance
        }
        return render(request, template, context)

######################################################################################## for edit your product item fr history edit and product edit
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('products.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'products/post_edit.html', {'form': form })


########################################################################################## show the list of login user donate items history
@login_required
def post_history(request):
    model = Product
    posts = Product.objects.filter(user_id = request.user.id)
    return render(request, 'products/post_list.html', {'posts': posts })


################################################################################## detail of perticular donate items have experidate ....

@login_required
def post_detail_history(request, pk):
    model = Product
    user_id=request.user.id
    post = get_object_or_404(Product, user_id=request.user.id, pk=pk)
    return render(request, 'products/product_detail_history.html', {'post': post })

########################################################################################## show detail of recent donateitem
@login_required
def list(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Product(user = request.user, title = request.POST['title'], docfile = request.FILES['docfile'], active = request.POST['active'], description = request.POST['description'], quantity = request.POST['quantity'], zip_Code = request.POST['zip_Code'], address = request.POST['address'], expire_date = request.POST['expire_date'])
            newdoc.save()
            return HttpResponseRedirect(reverse('products:post_detail_list',args=(post.pk,)))
    else:
        form = ProductForm() # A empty, unbound form

   # Load documents for the list page

    return render_to_response(
        'products/list.html',
        { 'form': form},
        context_instance=RequestContext(request)
    )

##################################################################################
@login_required
def post_detail_list(request, pk):
    model = Product
    user_id=request.user.id
    #post = Product.objects.filter(user_id = request.user.id, pk=pk)
    post = get_object_or_404(Product, user_id=request.user.id, pk=pk)
    return render(request, 'products/product_detail1.html', {'post': post })


################################################################################## edit form for history item
@login_required
def post_edit_list(request, pk):
    post = get_object_or_404(Product, user_id=request.user.id, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post )
        if form.is_valid():
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('products:post_detail_list',args=(post.pk,)))

    else:
        form = PostForm(instance=post)
    return render(request, 'products/post_edit.html', {'form': form })

