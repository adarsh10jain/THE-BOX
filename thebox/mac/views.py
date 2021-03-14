

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact,Order


def index(request):
    products=Product.objects.all()
    n=len(products)
    params = {'product':products}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse("we are at about")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        subject=request.POST.get('subject','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        contact.save()
    return render(request,"contact.html")

def categories(request):
    return render(request,"categories.html")

def search(request):
    return HttpResponse("we are at the search")

def productview(request,myid):
    #fetchb the product using id
    product=Product.objects.filter(id=myid)
    allproducts=Product.objects.all()

    return render(request,'product.html',{'product':product[0],'allproducts':allproducts})


def cart(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'cart.html', {'thank':thank, 'id': id})
    return render(request, 'cart.html')