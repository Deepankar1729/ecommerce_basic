import stripe
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import Products,Order

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
             user = form.save(commit = False)
             user.set_password(form.cleaned_data['password1'])
             user.save()
             login(request, user)
             return redirect('home')
    else:
          form = UserRegistrationForm()
     
    return render(request, 'registration/register.html', {'form': form})


@login_required
@never_cache
def home(request):
    products = Products.objects.filter(active = True)
    orders = Order.objects.filter(user = request.user, paid = True)
    return render(request, "products.html", {"products": products, "orders": orders})

@login_required
def checkout(request, product_id):
    product = get_object_or_404(Products, id = product_id, active = True)

    quantity = int(request.POST.get("quantity", 1))
    if quantity < 1:
        quantity = 1

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{

            "price_data": 
            {
                "currency": "usd",
                "product_data": {"name": product.name},
                "unit_amount": product.price,
            },
            "quantity": quantity,

        }],
        
        mode="payment",
        success_url="http://127.0.0.1:8000/success/?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="http://127.0.0.1:8000/home/",
    )

    return redirect(session.url)

@login_required
def success(request):
    session_id = request.GET.get("session_id")
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == "paid":
            line_items = stripe.checkout.Session.list_line_items(session.id, limit = 1)
            product_name = line_items.data[0].description if line_items.data else "Product"
            quantity = line_items.data[0].quantity if line_items.data else 1

            Order.objects.get_or_create(
                stripe_session_id = session.id,
                defaults = {
                    "user": request.user,
                    "product_name": product_name,
                    "amount": session.amount_total,
                    "quantity": quantity,
                    "paid": True,
                }
            )
    return render(request, 'success.html')