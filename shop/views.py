from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import ProductModule,Contact

# Create your views here.
def index(request):
    products = ProductModule.objects.all()
    context = {
        "products": products
    }
    return render(request,'index.html', context)

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'register.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists():
            print("User Already Exists")
        elif User.objects.filter(email=request.POST['email']).exists():
            print("Email Already Existed")
        else:
            u = User.objects.create_user(username=request.POST['username'],
                                         email=request.POST['email'],
                                         password=request.POST['password'])
            u.save()
            return redirect('login')
    else:
        return render(request, 'register.html')

@login_required
def cart(request, pk=None):
    products = ProductModule.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        # Get the current cart from the session or create an empty cart
        cart = request.session.get('cart', {})

        # Check if the product is already in the cart
        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            # If the product is not in the cart, add it
            product = ProductModule.objects.get(pk=product_id)
            cart[product_id] = {
                'id': product.id,
                'title': product.title,
                'image': product.image.url,
                'price': product.price,
                'quantity': quantity,
                'total_price': product.price * quantity,
            }

        # Update the cart in the session
        request.session['cart'] = cart
        return redirect('cart', pk=product_id)

    cart_items = request.session.get('cart', {}).values()
    grand_total = sum(item['total_price'] for item in cart_items)
    grand_total_adding_charges = max(0, grand_total + 500)
    return render(request, 'cart.html', {'cart_items': cart_items, 'products': products, 'grand_total': grand_total, 'grand_total_adding_charges': grand_total_adding_charges})

@login_required
def details(request,pk = None):
    products = ProductModule.objects.all()
    prod = ProductModule.objects.get(id = pk)
    context = {
        'product': prod,
        'products' : products
    }
    return render(request,'details.html', context)

@login_required
def products(request):
    products = ProductModule.objects.all()
    context = {
        "products": products
    }
    return render(request,'products.html',context)


def contact(request):
    if request.method == 'POST':
        data = Contact.objects.create(name=request.POST['name'],
                                      email=request.POST['email'],
                                      message=request.POST['message'])
        data.save()
        return redirect('index')
    else:
        return render(request, 'contact.html')