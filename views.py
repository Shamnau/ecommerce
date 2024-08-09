from django.conf.urls.static import static
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages




from .models import product
from .models import Address
from .models import Carts
from .models import Orders
# from .models import Orders

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def chocolate(request):
    return render(request,'chocolate.html')
def testimonial(request):
    return render(request,'testimonial.html')

def pro(request):
    d = product.objects.all()
    if request.method == 'POST':
        productname = request.POST['productname']
        print(productname)

        price = request.POST['price']
        print(price)

        image= request.FILES['image']
        print(image)

        f = product.objects.create(productname=productname, price=price, image=image)
        f.save()
    return render(request, 'product.html', {'e': d})

def viewproduct(request):
    x= product.objects.all()
    return render(request,'edit.html',{'y':x})

def edit(request,id):
    a = product.objects.get(id=id)
    if request.method=='POST':
        a.productname=request.POST['productname']
        a.price=request.POST['price']
        a.image=request.FILES['image']
        a.save()
    return redirect('viewproduct')
    return render(request, 'editproduct.html', {'b': a})

def delete(request, id):
    a = product.objects.get(id=id)
    a.delete()
    return redirect('pro')



def signup(request):

    if request.method == 'POST':
        email = request.POST['email']
        print(email)

        psw = request.POST['pass']
        print(psw)

        password= request.POST['pass']
        username=request.POST['email']
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('loginpage')
    return render(request,'signup.html')



def loginpage(request):
    if request.method == 'POST':
        userid = request.POST['email']
        print(userid)


        passw = request.POST['pass']
        print(passw)


        user = authenticate(username=userid,password=passw)
        if user is not None:
            login(request, user)
            print('login')
        else:
            print('incorrect')
        return  redirect('index')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return render(request,'login.html')


def proview(request,id):
    k = product.objects.get(id=id)
    print(k)
    if request.method == 'POST':

        f = Carts.objects.create(product=k, price=k.price, image=k.image,quantity=1,user=request.user)
        f.save()
    return render(request, 'proview.html', {'b': k})


def cart(request):
    y=Carts.objects.all()
    return render(request,'cart.html',{'u':y})

def removecart(request, id):
    a = Carts.objects.get(id=id)
    a.delete()
    return redirect('cart')


def shipping(request):
    m =Address.objects.all()
    if request.method == 'POST':
        user = request.POST['user']
        print(user)

        street_address = request.POST['street_address']
        print(street_address)

        city = request.POST['city']
        print(city)

        state = request.POST['state']
        print(state)

        zip_code = request.POST['zip_code']
        print(zip_code)

        country = request.POST['country']
        print(country)

        f = Address.objects.create(user=request.user, street_address=street_address, city=  city,  state=state,zip_code=zip_code, country= country)
        f.save()
    return render(request, 'address.html', {'e': m})

def orders(request):
    c=Address.objects.filter(user=request.user)
    z = Carts.objects.filter(user=request.user)
    return render(request, 'orders.html',{'b':z,'d':c})




def editaddr(request):
    r =Address.objects.get(user=request.user)
    if request.method=='POST':
        r.street_address=request.POST['street_address']
        r.city=request.POST['city']
        r.state=request.POST['state']
        r.zip_code=request.POST['zip_code']
        r.country=request.POST['country']
        r.save()
        return redirect('orders')
    return render(request, 'editaddr.html', {'d': r})

def deleteaddr(request,id):
    r = Address.objects.get(id=id)
    r.delete()
    return redirect('orders')

def orderconf(request):
    c = Address.objects.get(user=request.user)
    print(c)
    z = Carts.objects.filter(user=request.user)
    for i in z:
        f = Orders.objects.create(user=request.user,product=i.product, price=i.price,address=c, quantity=i.quantity)
        f.save()

        z.delete()
    return redirect('orders')

