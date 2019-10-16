from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product,Order,Update
from shop.models import Contact
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    
    products=product.objects.all()
    n=len(products)
    nslide=n//3+ceil((n/3)-(n//3))
    # allpro=[[products,range(len(products)),nslide]]
    # params={'allpro':allpro}
    params={'pro':products,"no":nslide,'range':range(1,nslide)}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')


def contact(request):
    thank=False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email',"")
        phone=request.POST.get('phone',"")
        query=request.POST.get('textarea','')
        contact=Contact(name=name,email=email,phone=phone,desc=query)
        contact.save()
        thank=True
    return render(request,'shop/contact.html',{'thank':thank})


def prodView(request,id):
    
    pro=product.objects.filter(id=id)
    return render(request,'shop/product.html',{'pro':pro[0]})



def searchmatch(query,item):
    if query.lower() in item.pro_name.lower() or query.lower() in item.desc.lower() or query.lower() in item.subcategory.lower() or query.lower() in item.category.lower():
        return True
    return False
def search(request):
    query=request.GET.get('search','')
    # print(query)
    print(query.lower())
    products=product.objects.all()
    print(products)
    proditem=[i for i in products if searchmatch(query,i)]
    
    params={'pro':proditem,'msg':""}
    if len(proditem)==0:
        params['msg']="Please Enter proper query"
    print(params)
    return render(request,'shop/search.html',params)

def tracker(request):
    if request.method=="POST":
        order_id=request.POST.get('Order_id','')
        email=request.POST.get('email','')
        
        try:
            tracker=Order.objects.filter(order_id=order_id,email=email)
            
            if len(tracker)>0:
                update=Update.objects.filter(order_id=order_id)

                udpates=[]
                for item in update:
                    udpates.append({'text':item.update_desc,'id':item.update_id})
                res=json.dumps(udpates)
                return HttpResponse(res)
            else:
                return render(request,'shop/tracker.html')                
        except Exception as e:
            print(e)

    else:

        return render(request,'shop/tracker.html')


def checkout(request):
    products1=product.objects.all()
        
    params1={'pro':products1}
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email',"")
        amount=request.POST.get('amount',"")
        address=request.POST.get('address',"")
        address2=request.POST.get('address2',"")
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip','')
        order=Order(name=name,email=email,add=address,add2=address2,city=city,state=state,zip_code=zip_code,price=amount)
        order.save()
        update=Update(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        
        return render(request,'shop/checkout.html',params1)
    return render(request,'shop/checkout.html',params1)

# def handlerrequest(request):
    # Paytm will send post request here.
    